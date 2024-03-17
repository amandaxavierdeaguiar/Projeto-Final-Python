from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
# from models.Supplier import Supplier
# from models.Category import Category
# from models.Stock import Stocks


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bar_cod: str = Field(unique=True)
    name: str
    description: str
    quantity: float
    price: float
    supplier_id: int = Field(default=None, foreign_key="supplier.id")
    category_id: int = Field(default=None, foreign_key="category.id")
    # supplier: Optional[Supplier] = Relationship(back_populates="supplier")
    # category: Optional[Category] = Relationship(back_populates="category")
    # stocks: List['Stocks'] = Relationship(back_populates="product") #Ver como vai ficar no banco
    """
        Ligaçao ao stocks fica no stocks

        Podemos deixar supplier aqui ou criar class Brand onde nela e que tem o supplier e aqui temos o brand_id    
    """
