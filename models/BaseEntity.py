from abc import ABC
from typing import Generic, TypeVar, Optional
from sqlmodel import Field, SQLModel


T = TypeVar('T')

class BaseEntity(SQLModel, ABC, Generic[T]):
    id: Optional[int] = Field(default=None, primary_key=True)
    