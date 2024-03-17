from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

# from models.Movement import Movement


class Supplier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str
    phone: str
    email: str
    # smovements: Optional[List['Movement']] = Relationship(back_populates="suppliers")
