from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from models.Product import Product
from models.Supplier import Supplier


class Movements(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    supplier_id: Optional[int] = Field(default=None, foreign_key="supplier.id")
    #bar_cod: str
    date: datetime
    quantity: float
    type_movement: str
    product: Optional['Product'] = Relationship(back_populates="movements")
    product: Optional['Supplier'] = Relationship(back_populates="supplier")


"""class Movements(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    #bar_cod: str
    date: datetime
    quantity: float
    type_movement: str"""