from controllers.BrandController import BrandController
from controllers.CategoryController import CategoryController
from controllers.MovementController import MovementController
from controllers.ProductController import ProductController
from controllers.StockController import StockController
from controllers.SupplierController import SupplierController
from controllers.UserController import UserController


def main():
    UserController()
    SupplierController()
    ProductController()
    CategoryController()
    StockController()
    BrandController()
    MovementController()
    # create_db_and_tables()


if __name__ == '__main__':
    main()
