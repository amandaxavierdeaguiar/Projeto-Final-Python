from models.Repository.BaseRepository import BaseRepository
from models.Category import Category
from models.db.db_conection import engine
from sqlmodel import Session, select


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session):
        super().__init__(session)

    def add(self, entity: Category) -> None:
        return super().add(entity)
    
    def getAll(self, entity: Category):
        return super().getAll(entity)
    
    def getById(self, entity: Category) -> Category:
        return super().getById(entity)
    
    def update(self, entity: Category) -> None:
        return super().update(entity)
    
    def delete(self, entity: Category) -> None:
        return super().delete(entity)
