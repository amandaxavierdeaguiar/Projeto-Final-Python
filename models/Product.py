from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from models.Supplier import Supplier
from models.Category import Category
from typing import List
from models.Stock import Stocks

class Product(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    bar_cod: str = Field(unique=True)
    name: str
    description: str
    quantity: int
    price: float
    supplier_id: Optional[int] = Field(default=None, foreign_key="supplier.id")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    supplier: Optional[Supplier] = Relationship(back_populates="products")
    category: Optional[Category] = Relationship(back_populates="products")
    stocks: List['Stocks'] = Relationship(back_populates="product") #Ver como vai ficar no banco



"""class Product(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    bar_cod: str = Field(unique=True)
    name: str
    description: str
    quantity: int
    price: float
    supplier: Optional['Supplier'] = None
    category: Optional['Category'] = None"""