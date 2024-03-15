from typing import Optional
from sqlmodel import Field, SQLModel


class Supplier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str
    phone: str
    email: str
