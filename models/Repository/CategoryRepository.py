from sqlmodel import select

from models.Category import Category
from models.Repository.BaseRepository import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Category, session_) -> None:
        session_.add(entity)
        session_.commit()
        session_.refresh(entity)

    @classmethod
    def get_all(cls, session_):
        statement = select(Category)
        result = session_.exec(statement).all()
        return result

    @classmethod
    def get_by_id(cls, entity: Category, session_) -> Category:
        statement = select(entity).where(entity.id == entity.id)
        result = session_.exec(statement)
        return result

    @classmethod
    def update(cls, entity: Category, session_) -> None:
        statement = select(entity).where(entity.id == entity.id)
        exec_result = session_.exec(statement)
        result = exec_result.one()

        result = entity
        session_.add(result)
        session_.commit()
        session_.refresh(result)

    @classmethod
    def delete(cls, entity: Category, session_) -> None:
        statement = select(entity).where(entity.id == entity.id)
        exec_result = session_.exec(statement)
        result = exec_result.one()

        session_.delete(result)
        session_.commit()

        statement = select(entity).where(entity.id == entity.id)
        exec_confirm = session_.exec(statement)
        result_confirm = exec_confirm.first()

        if result_confirm is None:
            print("Successfully Deleted")
