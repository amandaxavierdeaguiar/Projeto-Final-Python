from controllers.BaseController import BaseController
from models.Repository.UserRepository import UserRepository
from models.User import User


class UserController(BaseController[User]):
    repo: UserRepository = UserRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: User, session_):
        cls.repo.add(entity, session_)

    @classmethod
    def get_all(cls, session_):
        return cls.repo.get_all(session_)

    @classmethod
    def get_by_email(cls, email: str, session_):
        return cls.repo.get_by_email(email, session_)

    @classmethod
    def get_by_id(cls, entity: User, session_):
        return cls.repo.get_by_id(entity, session_)

    @classmethod
    def update(cls, entity: User, session_) -> None:
        cls.repo.update(entity, session_)

    @classmethod
    def delete(cls, entity: User, session_) -> None:
        cls.repo.delete(entity, session_)

    @classmethod
    def authenticate_user(cls, email, password, session_):
        result = cls.get_by_email(email, session_)
        if result:
            if result.password == password:
                return True
            else:
                return False
        else:
            return False
