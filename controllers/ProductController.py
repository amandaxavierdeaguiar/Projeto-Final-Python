from controllers.BaseController import BaseController
from models.Product import Product
from models.Repository.ProductRepository import ProductRepository


class ProductController(BaseController[Product]):
    repo: ProductRepository = ProductRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Product, session_) -> None:
        cls.repo.add(entity, session_)

    @classmethod
    def get_all(cls, session_):
        return cls.repo.get_all(session_)

    @classmethod
    def get_all_join(cls, session_):
        return cls.repo.get_all_join(session_)

    @classmethod
    def get_by_id(cls, entity: Product, session_) -> Product:
        return cls.repo.get_by_id(entity, session_)

    @classmethod
    def update(cls, entity: Product, session_) -> None:
        cls.repo.update(entity, session_)

    @classmethod
    def delete(cls, entity: Product, session_) -> None:
        cls.repo.delete(entity, session_)
