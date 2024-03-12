from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional
from models.db import create_db_and_tables, engine, select
from sqlmodel import Session

T = TypeVar('T')


class BaseRepository(ABC, Generic[T]):
    
    @abstractmethod 
    def add(self, entity: T) -> None:
        with Session(engine) as session:
            session.add(T)
            session.commit()
            session.refresh(T)

    @abstractmethod 
    def getAll(self, entity: T):
        with Session(engine) as session:
            statement = select(T)
            result = session.exec(statement).all()
            return result
    
    @abstractmethod 
    def getById(self, entity: T) -> T:
        with Session(engine) as session:
            statement = select(T).where(T.id == T.id)
            result = session.exec(statement)
            return result

    @abstractmethod 
    def update(self, entity: T) -> None:
        prefix = "old_"
        with Session(engine) as session:
            statement = select(T).where(T.id == T.id)
            exec_result = session.exec(statement)
            result = exec_result.one()
   
            result = T
            session.add(result)
            session.commit()
            session.refresh(result)
    
    @abstractmethod 
    def delete(self, entity: T) -> None:
        with Session(engine) as session:
            statement = select(T).where(T.id == T.id)
            exec_result = session.exec(statement)  
            result = exec_result.one()   

            session.delete(result)  
            session.commit()  

            statement = select(T).where(T.id == T.id)
            exec_confirm = session.exec(statement)  
            result_confirm = exec_confirm.first()  

        if result_confirm is None:  
            print("Successfully Deleted")  
    