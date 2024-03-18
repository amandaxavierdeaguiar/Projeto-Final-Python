from typing import Optional

from sqlmodel import Field, SQLModel


class Brand(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    supplier_id: int = Field(default=None, foreign_key="supplier.id")
