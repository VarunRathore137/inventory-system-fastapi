from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    sku: str
    qty: int = 0
    price: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
