from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import List
from models.Product import Product


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    # products: List['Product'] = Relationship(back_populates="category")
    """ Penso nao precisar da lista de produtos a qual estão assossiados porque isso
    e obtido pelo um select
     
    Isto se a lista não for algo interno ao SQLModel e por isso e que precisa de estar """
