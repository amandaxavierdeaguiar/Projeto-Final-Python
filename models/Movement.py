from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

# from models.Product import Product
# from models.Supplier import Supplier


class Movement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(default=None, foreign_key="product.id")
    supplier_id: Optional[int] = Field(default=None, foreign_key="supplier.id")
    user_id: int = Field(default=None, foreign_key="user.id")
    date: datetime
    quantity: float
    type_movement: str
    # products: Optional[Product] = Relationship(back_populates="movements")
    # suppliers: Optional[Supplier] = Relationship(back_populates="movements")

    """
        Penso que supplier_id é o unico que pode ser optional 
        porque ao fazer uma alteração no stock(mudança da quantidade por ter sido vendido)
        o movimento vem do stock e por isso nao terá supplier

        adicionei user_id para ficar resistado qual user vez certo movimento

    """
