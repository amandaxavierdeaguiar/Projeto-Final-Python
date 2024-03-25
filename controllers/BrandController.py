from controllers.BaseController import BaseController
from models.Brand import Brand
from models.Repository.BrandRepository import BrandRepository


class BrandController(BaseController[Brand]):
    repo: BrandRepository = BrandRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Brand, session_) -> None:
        pass

    @classmethod
    def get_all(cls, session_):
        return cls.repo.get_all(session_)

    @classmethod
    def get_by_id(cls, entity: Brand, session_) -> Brand:
        pass

    @classmethod
    def get_by_name(cls, name: str, session_) -> Brand:
        return cls.repo.get_by_name(name, session_)

    @classmethod
    def update(cls, entity: Brand, session_) -> None:
        pass

    @classmethod
    def delete(cls, entity: Brand, session_) -> None:
        pass
