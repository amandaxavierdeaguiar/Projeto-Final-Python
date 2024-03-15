from controllers.UserController import UserController
from controllers.SupplierController import SupplierController
from controllers.StockController import StockController
from controllers.ProductController import ProductController
from controllers.CategoryController import CategoryController
from models.db.db_conection import get_session
from models.User import User
from models.Enums.TypeAccess import TypeAccess


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

