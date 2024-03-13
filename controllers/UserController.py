from models.Enums.TypeAcess import TypeAcess
from models.Repository.UserRepository import UserRepository
from models.User import User

class UserController():
    def add():
        cnt = UserRepository()
        u = User("fabio@email.com", "test1234", "fabio", TypeAcess.User)
        cnt.add(u)