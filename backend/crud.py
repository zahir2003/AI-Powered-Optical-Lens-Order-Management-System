from sqlalchemy.orm import Session

import models

# -----------------------
# INVENTORY
# -----------------------


def create_inventory(db: Session, inventory):

    existing_inventory = (
        db.query(models.Inventory)
        .filter(
            models.Inventory.lens_type == inventory.lens_type,
            models.Inventory.power == inventory.power,
            models.Inventory.lens_index == inventory.lens_index,
            models.Inventory.coating == inventory.coating,
        )
        .first()
    )

    # If same inventory already exists,
    # increase quantity instead of creating new row
    if existing_inventory:

        existing_inventory.quantity += inventory.quantity

        db.commit()

        db.refresh(existing_inventory)

        return existing_inventory

    # Otherwise create new inventory record
    db_inventory = models.Inventory(
        lens_type=inventory.lens_type,
        power=inventory.power,
        lens_index=inventory.lens_index,
        coating=inventory.coating,
        quantity=inventory.quantity,
    )

    db.add(db_inventory)

    db.commit()

    db.refresh(db_inventory)

    return db_inventory


def get_inventory(db: Session):

    return db.query(models.Inventory).all()


# -----------------------
# ORDERS
# -----------------------


def create_order(db: Session, order):

    inventory_items = (
        db.query(models.Inventory)
        .filter(models.Inventory.lens_type == order.lens_type)
        .all()
    )

    inventory_item = None

    for item in inventory_items:

        if (
            round(item.power, 2) == round(order.power, 2)
            and round(item.lens_index, 2) == round(order.lens_index, 2)
            and item.coating == order.coating
            and item.quantity > 0
        ):
            inventory_item = item
            break

    inventory_available = False

    # -----------------------
    # SLA BY LENS TYPE
    # -----------------------

    if order.lens_type == "Single Vision":
        sla_hours = 24

    elif order.lens_type == "Progressive":
        sla_hours = 48

    else:  # Bifocal
        sla_hours = 72

    # -----------------------
    # INVENTORY CHECK
    # -----------------------

    if inventory_item and inventory_item.quantity >= order.quantity:

        inventory_available = True

        inventory_item.quantity -= order.quantity

    else:

        inventory_available = False

        # Manufacturing required
        sla_hours += 24

    db_order = models.Order(
        customer_name=order.customer_name,
        store_location=order.store_location,
        lens_type=order.lens_type,
        power=order.power,
        lens_index=order.lens_index,
        coating=order.coating,
        frame=order.frame,
        quantity=order.quantity,
        status="Order Placed",
        inventory_available=inventory_available,
        sla_hours=sla_hours,
        elapsed_hours=0,
    )

    db.add(db_order)

    db.commit()

    db.refresh(db_order)

    return db_order


def get_orders(db: Session):

    return db.query(models.Order).all()


def update_order_status(
    db: Session,
    order_id: int,
    status: str,
    delay_reason: str = None,
):

    order = db.query(models.Order).filter(models.Order.id == order_id).first()

    if not order:
        return None

    order.status = status

    # Clear old delay reason when workflow continues
    if status != "QC Failed":
        order.delay_reason = None

    if delay_reason:
        order.delay_reason = delay_reason

    # -----------------------
    # PROCESS FLOW
    # -----------------------

    if status == "Production":

        if order.lens_type == "Single Vision":
            order.elapsed_hours += 8

        elif order.lens_type == "Progressive":
            order.elapsed_hours += 16

        elif order.lens_type == "Bifocal":
            order.elapsed_hours += 32

    elif status == "QC":

        if order.lens_type == "Single Vision":
            order.elapsed_hours += 4

        elif order.lens_type == "Progressive":
            order.elapsed_hours += 8

        elif order.lens_type == "Bifocal":
            order.elapsed_hours += 12

    elif status == "QC Failed":

        order.status = "Reorder"

        order.delay_reason = "QC Failure - Reorder Required"

        if order.lens_type == "Single Vision":
            order.elapsed_hours += 20

        elif order.lens_type == "Progressive":
            order.elapsed_hours += 24

        elif order.lens_type == "Bifocal":
            order.elapsed_hours += 30

    elif status == "Reorder":

        if order.lens_type == "Single Vision":
            order.elapsed_hours += 8

        elif order.lens_type == "Progressive":
            order.elapsed_hours += 12

        elif order.lens_type == "Bifocal":
            order.elapsed_hours += 18

    elif status == "Packed":

        order.elapsed_hours += 3

    elif status == "Shipped":

        order.elapsed_hours += 2

    elif status == "Delivered":

        order.elapsed_hours += 1

        # Delivered orders should not appear in alerts
        order.predicted_breach = False
        order.predicted_confidence = 0

        if hasattr(order, "alert_sent"):
            order.alert_sent = False

    db.commit()

    db.refresh(order)

    return order
