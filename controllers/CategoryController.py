from models.Repository.CategoryRepository import CategoryRepository
from models.Category import Category

class CategoryController():
    def add(self):
        cnt = CategoryRepository()
        ct = Category('Categoria')
        cnt.add(ct)
        #cnt.update(ct)