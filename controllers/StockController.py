from controllers.BaseController import BaseController, T
from models.Repository.StockRepository import StocksRepository
from models.Stock import Stock


class StockController(BaseController[Stock]):
    def get_by_id(self, entity: T, session_) -> T:
        pass

    repo: StocksRepository = StocksRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Stock, session_) -> None:
        cls.repo.add(entity, session_)

    @classmethod
    def get_all(cls, session_):
        return cls.repo.get_all(session_)

    @classmethod
    def get_all_by_category(cls, session_, category) -> Stock:
        return cls.repo.get_all_by_category(session_, category)

    @classmethod
    def get_all_by_brand(cls, session_, brand) -> Stock:
        return cls.repo.get_all_by_brand(session_, brand)

    @classmethod
    def get_by_bar_code(cls, session_, bar_code) -> Stock:
        return cls.repo.get_by_bar_code(session_, bar_code)

    @classmethod
    def get_by_name(cls, session_, name) -> Stock:
        return cls.repo.get_by_name(session_, name)

    @classmethod
    def update(cls, entity: Stock, session_) -> None:
        cls.repo.update(entity, session_)

    @classmethod
    def delete(cls, entity: Stock, session_) -> None:
        cls.repo.delete(entity, session_)
