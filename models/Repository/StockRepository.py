from models.Repository.BaseRepository import BaseRepository
from models.Stock import Stocks

class StocksRepository(BaseRepository[Stocks]):
    def __init__(self, session):
        super().__init__(session)

    def add(self, entity: Stocks) -> None:
        return super().add(entity)
    
    def getAll(self, entity: Stocks):
        return super().getAll(entity)
    
    def getById(self, entity: Stocks) -> Stocks:
        return super().getById(entity)
    
    def update(self, entity: Stocks) -> None:
        return super().update(entity)
    
    def delete(self, entity: Stocks) -> None:
        return super().delete(entity)