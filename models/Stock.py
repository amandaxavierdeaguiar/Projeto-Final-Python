from typing import Optional
from sqlmodel import Field, SQLModel


class Stocks(SQLModel, table=False):
    pass