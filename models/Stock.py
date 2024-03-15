from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from models.Product import Product


class Stocks(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(default=None, foreign_key="product.id")
    quantity: float
    # product: Optional['Product'] = Relationship(back_populates="stocks")
    """ Penso nao precisar da lista de produtos a qual estão assossiados porque isso
    e obtido pelo um select 
    
    Isto se a lista não for algo interno ao SQLModel e por isso e que precisa de estar"""