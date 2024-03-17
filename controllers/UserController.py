from controllers.BaseController import BaseController
from models.Repository.UserRepository import UserRepository
from models.User import User


class UserController(BaseController[User]):
    repo: UserRepository = UserRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, u: User, session):
        cls.repo.add(u, session)

    @classmethod
    def get_all(cls, session_):
        return cls.repo.get_all(session_)

    @classmethod
    def get_by_id(cls, entity: User, session_):
        return cls.repo.get_by_id(entity, session_)

    @classmethod
    def update(cls, entity: User, session_) -> None:
        cls.repo.update(entity, session_)

    @classmethod
    def delete(cls, entity: User, session_) -> None:
        cls.repo.delete(entity, session_)
