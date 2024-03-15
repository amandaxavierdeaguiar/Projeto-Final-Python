from models.Enums.TypeAccess import TypeAccess
from models.Repository.UserRepository import UserRepository
from models.User import User


class UserController():
    def add(self):
        cnt = UserRepository()
        u = User("fabio@email.com", "test1234", "fabio", TypeAccess.User)
        cnt.add(u)
