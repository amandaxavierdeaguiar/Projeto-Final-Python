from typing import Optional
from sqlmodel import Field, SQLModel
from models.Enums.TypeAccess import TypeAccess


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    login: str
    password: str
    name: str
    typeAccess: TypeAccess = TypeAccess.User
