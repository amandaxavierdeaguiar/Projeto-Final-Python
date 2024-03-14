from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import List
from models.Product import Product

class Category(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    products: List['Product'] = Relationship(back_populates="category")
