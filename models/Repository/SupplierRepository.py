from sqlmodel import select

from models.Repository.BaseRepository import BaseRepository
from models.Supplier import Supplier


class SupplierRepository(BaseRepository[Supplier]):
    def __init__(self):
        super().__init__()

    def add(self, entity: Supplier, session_) -> None:
        session_.add(entity)
        session_.commit()
        session_.refresh(entity)

    def get_all(self, session_):
        statement = select(Supplier)
        result = session_.exec(statement).all()
        return result

    def get_by_id(self, entity: Supplier, session_) -> Supplier:
        statement = select(entity).where(entity.id == entity.id)
        result = session_.exec(statement)
        return result

    def update(self, entity: Supplier, session_) -> None:
        statement = select(entity).where(entity.id == entity.id)
        exec_result = session_.exec(statement)
        result = exec_result.one()

        result = entity
        session_.add(result)
        session_.commit()
        session_.refresh(result)

    def delete(self, entity: Supplier, session_) -> None:
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
