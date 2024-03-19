from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseRepository(Generic[T], ABC):

    def __init__(self):
        pass

    @abstractmethod
    def add(self, entity: T, session_) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_all(self, session_):
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, entity: T, session_) -> T:
        raise NotImplementedError()

    @abstractmethod
    def update(self, entity: T, session_) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, entity: T, session_) -> None:
        raise NotImplementedError()
