from controllers.BaseController import BaseController
from models.Movement import Movement
from models.Repository.MovementRepository import MovementRepository


class MovementController(BaseController[Movement]):
    repo: MovementRepository = MovementRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Movement, session_) -> None:
        pass

    @classmethod
    def get_all(cls, session_):
        pass

    @classmethod
    def get_by_id(cls, entity: Movement, session_) -> Movement:
        pass

    @classmethod
    def update(cls, entity: Movement, session_) -> None:
        pass

    @classmethod
    def delete(cls, entity: Movement, session_) -> None:
        pass
