from models.Repository.BaseRepository import BaseRepository
from models.Supplier import Supplier
from models.db.db_conection import engine
from sqlmodel import Session, select


class SupplierRepository(BaseRepository[Supplier]):
    def __init__(self, session):
        super().__init__(session)

    def add(self, entity: Supplier) -> None:
        return super().add(entity)
    
    def getAll(self, entity: Supplier):
        return super().getAll(entity)
    
    def getById(self, entity: Supplier) -> Supplier:
        return super().getById(entity)
    
    def update(self, entity: Supplier) -> None:
        return super().update(entity)
    
    def delete(self, entity: Supplier) -> None:
        return super().delete(entity)