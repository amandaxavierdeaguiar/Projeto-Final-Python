from controllers.BaseController import BaseController
from models.Repository.StockRepository import StocksRepository
from models.Stock import Stock


class StockController(BaseController[Stock]):
    repo: StocksRepository = StocksRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Stock, session_) -> None:
        pass

    @classmethod
    def get_all(cls, session_):
        pass

    @classmethod
    def get_by_id(cls, entity: Stock, session_) -> Stock:
        pass

    @classmethod
    def update(cls, entity: Stock, session_) -> None:
        pass

    @classmethod
    def delete(cls, entity: Stock, session_) -> None:
        pass
