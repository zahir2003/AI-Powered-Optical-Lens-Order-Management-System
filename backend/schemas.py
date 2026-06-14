from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ------------------------
# Inventory
# ------------------------


class InventoryCreate(BaseModel):
    lens_type: str
    power: float
    lens_index: float
    coating: str
    quantity: int


# ------------------------
# Order Creation
# ------------------------


class OrderCreate(BaseModel):
    customer_name: str
    store_location: str

    lens_type: str

    power: float

    lens_index: float

    coating: str

    frame: str

    quantity: int


# ------------------------
# Status Update
# ------------------------


class OrderUpdate(BaseModel):
    status: str
    delay_reason: Optional[str] = None


class InventoryResponse(BaseModel):
    id: int
    lens_type: str
    power: float
    quantity: int

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    status: str
    quantity: int
    inventory_available: bool
    sla_hours: int
    created_at: datetime

    class Config:
        from_attributes = True
