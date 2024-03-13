from typing import Optional
from sqlmodel import Field, SQLModel


class Product(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    bar_cod: str
    name: str
    description: str
    quantity: int
    price: float
    supplier: Optional['Supplier'] = None
    category: Optional['Category'] = None