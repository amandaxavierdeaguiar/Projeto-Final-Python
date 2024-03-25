from controllers.BaseController import BaseController, T
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
        return cls.repo.get_all(session_)

    def get_by_id(self, entity: T, session_) -> T:
        pass

    @classmethod
    def get_by_name(cls, name: str, session_) -> Category:
        return cls.repo.get_by_name(name, session_)

    @classmethod
    def update(cls, entity: Category, session_) -> None:
        pass

    @classmethod
    def delete(cls, entity: Category, session_) -> None:
        pass
