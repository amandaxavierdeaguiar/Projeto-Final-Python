from models.Enums.TypeAcess import TypeAcess
from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    login: str
    password: str
    name: str
    typeAcess : TypeAcess = TypeAcess.User