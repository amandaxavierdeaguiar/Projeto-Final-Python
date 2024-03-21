from sqlmodel import Session
from pydantic import ValidationError, BaseModel, model_validator

from models.Repository.UserRepository import UserRepository
from models.db.db_conection import get_session


class UserAuthentication:
    login: str
    password: str
    is_login: bool = False
    session: Session = get_session()

    @classmethod
    def check(cls, login_, password_):
        repo: UserRepository = UserRepository()
        u = repo.get_by_email(login_, cls.session)
        if (
            password_ is not None
            and login_ is not None
            and u is not None
            and password_ != u.password
        ):
            cls.is_login = False
            raise ValidationError("Login Incorreto")
        cls.is_login = True
