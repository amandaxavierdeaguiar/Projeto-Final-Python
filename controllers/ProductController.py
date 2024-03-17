from controllers.BaseController import BaseController
from models.Product import Product
from models.Repository.ProductRepository import ProductRepository


class ProductController(BaseController[Product]):
    repo: ProductRepository = ProductRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Product, session_) -> None:
        pass

    @classmethod
    def get_all(cls, session_):
        pass

    @classmethod
    def get_by_id(cls, entity: Product, session_) -> Product:
        pass

    @classmethod
    def update(cls, entity: Product, session_) -> None:
        pass

    @classmethod
    def delete(cls, entity: Product, session_) -> None:
        pass
