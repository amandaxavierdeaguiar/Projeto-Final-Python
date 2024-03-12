from models import BaseEntity
from typing import Optional


class Product(BaseEntity):
    bar_cod: str
    name: str
    description: str
    quantity: int
    price: float
    supplier: Optional['Supplier'] = None
    category: Optional['Category'] = None