from models.Repository.BaseRepository import BaseRepository
from models.Movement import Movements

class MovementsRepository(BaseRepository[Movements]):
    def __init__(self, session):
        super().__init__(session)

    def add(self, entity: Movements) -> None:
        return super().add(entity)
    
    def getAll(self, entity: Movements):
        return super().getAll(entity)
    
    def getById(self, entity: Movements) -> Movements:
        return super().getById(entity)
    
    def update(self, entity: Movements) -> None:
        return super().update(entity)
    
    def delete(self, entity: Movements) -> None:
        return super().delete(entity)