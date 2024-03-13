from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime


class Movements(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    bar_cod: str
    date: datetime
    quantity: float
    type_movement: str