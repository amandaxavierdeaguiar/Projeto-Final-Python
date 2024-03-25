from typing import Dict

from sqlmodel import Session
from pydantic import ValidationError

from models.Repository.UserRepository import UserRepository
from models.db.db_conection import get_session


class UserAuthentication:
    login: str
    password: str
    is_login: bool = False
    session: Session = get_session()
    permissions: Dict

    @classmethod
    def check(cls, login_, password_):
        repo: UserRepository = UserRepository()
        u = repo.get_by_email(login_, cls.session)
        cls.permissions = cls.give_permissions(u)
        if (
            password_ is not None
            and login_ is not None
            and u is not None
            and password_ != u.password
        ):
            cls.is_login = False
            raise ValidationError("Login Incorreto")
        cls.is_login = True

    @classmethod
    def give_permissions(cls, user):
        roles: Dict = {
            "Admin": {
                "User": ["Create", "Read", "Update", "Delete"],
                "Stock": ["Create", "Read", "Update", "Delete"],
                "Supplier": ["Create", "Read", "Update", "Delete"],
                "Product": ["Create", "Read", "Update", "Delete"],
            },
            "Sub_Admin": {
                "User": [],
                "Stock": ["Create", "Read", "Update"],
                "Supplier": ["Create", "Read", "Update"],
                "Product": ["Create", "Read", "Update"],
            },
            "User": {
                "User": [],
                "Stock": ["Read"],
                "Supplier": ["Read"],
                "Product": ["Read"],
            },
        }
        return roles[f"{user.typeAccess.value}"]
