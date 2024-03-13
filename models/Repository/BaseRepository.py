from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar('T')


class BaseRepository(Generic[T], ABC):

    def __init__(self, session):
        self.session = session
    
    @abstractmethod
    def add(self, entity: T) -> None:
        raise NotImplementedError()

    @abstractmethod 
    def getAll(self, entity: T):
        raise NotImplementedError()
    
    @abstractmethod 
    def getById(self, entity: T) -> T:
        raise NotImplementedError()

    @abstractmethod 
    def update(self, entity: T) -> None:
        raise NotImplementedError()
    
    @abstractmethod 
    def delete(self, entity: T) -> None:
        raise NotImplementedError()
    