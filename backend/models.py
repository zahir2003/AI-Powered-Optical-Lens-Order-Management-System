from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime

from database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)

    lens_type = Column(String)
    power = Column(Float)

    lens_index = Column(Float)
    coating = Column(String)

    quantity = Column(Integer)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String)

    store_location = Column(String)

    lens_type = Column(String)

    power = Column(Float)

    lens_index = Column(Float)

    coating = Column(String)

    frame = Column(String)

    quantity = Column(Integer, default=1)

    status = Column(String)

    inventory_available = Column(Boolean)

    sla_hours = Column(Integer)

    elapsed_hours = Column(Integer, default=0)

    delay_reason = Column(String, nullable=True)

    predicted_breach = Column(Boolean, default=False)

    predicted_confidence = Column(Float, default=0.0)

    alert_sent = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
