from models import BaseEntity
from models.Enums import TypeAcess


class User(BaseEntity):
    login: str
    password: str
    name: str
    typeAcess : TypeAcess = TypeAcess.User