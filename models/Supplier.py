from typing import Optional
from sqlmodel import Field, SQLModel



class Supplier(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    adress: str
    phone: str
    email: str