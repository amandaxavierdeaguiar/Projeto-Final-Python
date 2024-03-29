from pydantic import decorator

from controllers.MovementController import MovementController
from models.Movement import Movement
import datetime


class CallMovement:
    def __init__(self):
        pass

    def call_movement(func):
        def inner():
            is_finish, what_to_send = func()
            if is_finish:
                move = MovementController()
                m = Movement()
                m.product_id = what_to_send.id
                move.add()

        return inner


def call_movement():
    return None
