from controllers.BaseController import BaseController
from models.Category import Category
from models.Repository.CategoryRepository import CategoryRepository


class CategoryController(BaseController[Category]):
    repo: CategoryRepository = CategoryRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Category, session_) -> None:
        pass

    @classmethod
    def get_all(cls, session_):
        pass

    @classmethod
    def get_by_id(cls, entity: Category, session_) -> Category:
        pass

    @classmethod
    def update(cls, entity: Category, session_) -> None:
        pass

    @classmethod
    def delete(cls, entity: Category, session_) -> None:
        pass
