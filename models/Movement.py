from models import BaseEntity
from datetime import datetime


class Movements(BaseEntity):
    bar_cod: str
    date: datetime
    quantity: float
    type_movement: str