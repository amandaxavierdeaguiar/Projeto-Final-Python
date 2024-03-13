from typing import Optional
from sqlmodel import Field, SQLModel


class Category(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str