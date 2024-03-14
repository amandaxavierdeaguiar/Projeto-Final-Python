from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from models.Product import Product


class Stocks(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    quantity: int
    product: Optional['Product'] = Relationship(back_populates="stocks")