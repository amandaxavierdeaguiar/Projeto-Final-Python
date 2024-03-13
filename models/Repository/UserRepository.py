from models.Repository.BaseRepository import BaseRepository
from models.User import User
from models.db import engine
from sqlmodel import Session, select


class UserRepository(BaseRepository[User]):
    def __init__(self, session):
        super().__init__(session)   

    def add(self, entity: User) -> None:
        with Session(engine) as session:
            session.add(User)
            session.commit()
            session.refresh(User)
    
    def getAll(self, entity: User):
        with Session(engine) as session:
            statement = select(User)
            result = session.exec(statement).all()
            return result
    
    def getById(self, entity: User) -> User:
        with Session(engine) as session:
            statement = select(User).where(User.id == User.id)
            result = session.exec(statement)
            return result
    
    def update(self, entity: User) -> None:
        with Session(engine) as session:
            statement = select(User).where(User.id == User.id)
            exec_result = session.exec(statement)
            result = exec_result.one()
   
            result = User
            session.add(result)
            session.commit()
            session.refresh(result)
    
    def delete(self, entity: User) -> None:
        with Session(engine) as session:
            statement = select(User).where(User.id == User.id)
            exec_result = session.exec(statement)  
            result = exec_result.one()   

            session.delete(result)  
            session.commit()  

            statement = select(User).where(User.id == User.id)
            exec_confirm = session.exec(statement)  
            result_confirm = exec_confirm.first()  

        if result_confirm is None:  
            print("Successfully Deleted")  