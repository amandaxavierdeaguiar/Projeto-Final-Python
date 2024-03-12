from models import BaseEntity



class Supplier(BaseEntity):
    name: str
    adress: str
    phone: str
    email: str