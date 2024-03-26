from sqlmodel import Session

from controllers.UserController import UserController
from models.User import User
from models.db.db_conection import get_session


class RegistrationView:
    is_login: bool = None
    ctrl_user: UserController = UserController()
    session: Session = get_session()
    error_txt: str = ""

    def __init__(self):
        super().__init__()

    @classmethod
    def give_frame(cls, app_):
        pass

    @classmethod
    def create_user(cls):
        u = User()
        cls.ctrl_user.add(u, cls.session)
