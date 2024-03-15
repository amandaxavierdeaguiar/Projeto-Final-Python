from models.Repository.CategoryRepository import CategoryRepository
from models.Category import Category


class CategoryController:
    def __init__(self):
        pass

    @classmethod
    def add(cls, ct: Category, session):
        cnt = CategoryRepository()
        Category('Categoria')
        cnt.add(ct, session)
        # cnt.update(ct)
