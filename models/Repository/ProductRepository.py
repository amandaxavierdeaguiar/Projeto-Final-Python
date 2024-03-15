from models.Repository.BaseRepository import BaseRepository
from models.Product import Product

class ProductRepository(BaseRepository[Product]):
    def __init__(self, session):
        super().__init__(session)

    def add(self, entity: Product) -> None:
        return super().add(entity)
    
    def getAll(self, entity: Product):
        return super().getAll(entity)
    
    def getById(self, entity: Product) -> Product:
        return super().getById(entity)
    
    def update(self, entity: Product) -> None:
        return super().update(entity)
    
    def delete(self, entity: Product) -> None:
        return super().delete(entity)