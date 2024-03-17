from controllers.CategoryController import CategoryController
from controllers.ProductController import ProductController
from controllers.StockController import StockController
from controllers.SupplierController import SupplierController
from controllers.UserController import UserController


def main():
    UserController()
    # u = User(login="fabio@email.com", password="1234test", name="fabio")
    # UserController.add(u, get_session())
    # u = User()
    # u = UserController.get_all(get_session())
    SupplierController()
    ProductController()
    CategoryController()
    StockController()


if __name__ == '__main__':
    main()
    # create_db_and_tables()
