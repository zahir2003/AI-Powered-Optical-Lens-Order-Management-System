from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, get_db
from utils import calculate_remaining_time
from ml_service import predict_breach
from scheduler import scheduler

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Order Management System")
scheduler.start()


@app.get("/")
def home():
    return {"message": "AI Order Management System Running"}


# ---------------------------------
# INVENTORY
# ---------------------------------


@app.post("/inventory")
def add_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory(db, inventory)


@app.get("/inventory")
def get_inventory(db: Session = Depends(get_db)):
    return crud.get_inventory(db)


# ---------------------------------
# ORDERS
# ---------------------------------


@app.post("/orders")
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)


@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)


@app.put("/orders/{order_id}")
def update_order(
    order_id: int, update: schemas.OrderUpdate, db: Session = Depends(get_db)
):
    order = crud.update_order_status(db, order_id, update.status, update.delay_reason)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):

    orders = crud.get_orders(db)

    result = []

    for order in orders:

        remaining = calculate_remaining_time(order)

        result.append(
            {
                "id": order.id,
                "customer": order.customer_name,
                "status": order.status,
                "sla_hours": order.sla_hours,
                "remaining_hours": remaining,
                "breached": remaining < 0,
            }
        )

    return result


@app.get("/alerts")
def get_alerts(db: Session = Depends(get_db)):

    orders = crud.get_orders(db)

    alerts = []

    for order in orders:

        # Skip delivered orders completely
        if order.status == "Delivered":
            continue

        if order.predicted_confidence >= 50:

            alerts.append(
                {
                    "order_id": order.id,
                    "customer": order.customer_name,
                    "status": order.status,
                    "confidence": order.predicted_confidence,
                    "risk": (
                        "HIGH"
                        if order.predicted_confidence >= 80
                        else "MEDIUM"
                    ),
                }
            )

        if order.predicted_confidence >= 80:
            print(f"ALERT: Order {order.id} may breach SLA")

    return alerts
