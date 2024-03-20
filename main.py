from controllers.BrandController import BrandController
from controllers.CategoryController import CategoryController
from controllers.MovementController import MovementController
from controllers.ProductController import ProductController
from controllers.StockController import StockController
from controllers.SupplierController import SupplierController
from controllers.UserController import UserController
from views.MainView import MainView
from view.stockApp import StockView
from models.User import User
from models.db.db_conection import get_session


def main():
    MainView()

    """UserController()
    SupplierController()
    ProductController()
    CategoryController()
    StockController()
    BrandController()
    MovementController()"""
    # create_db_and_tables()


if __name__ == '__main__':
    main()
