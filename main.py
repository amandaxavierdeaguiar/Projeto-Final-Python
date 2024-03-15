from models.db.db_conection import create_db_and_tables
from controllers.UserController import UserController
from controllers.SupplierController import SupplierController
from controllers.StockController import StockController
from controllers.ProductController import ProductController
from controllers.CategoryController import CategoryController

def teste():
    UserController()
    SupplierController()
    StockController()
    ProductController()
    CategoryController()
    
if __name__ == '__main__':
    create_db_and_tables()
    teste()

