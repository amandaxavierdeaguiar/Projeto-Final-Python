from controllers.BaseController import BaseController
from models.Repository.SupplierRepository import SupplierRepository
from models.Supplier import Supplier


class SupplierController(BaseController[Supplier]):
    repo: SupplierRepository = SupplierRepository()

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Supplier, session_) -> None:
        pass

    @classmethod
    def get_all(cls, session_):
        return cls.repo.get_all(session_)

    @classmethod
    def get_by_id(cls, entity: Supplier, session_) -> Supplier:
        pass

    @classmethod
    def update(cls, entity: Supplier, session_) -> None:
        pass

    @classmethod
    def delete(cls, entity: Supplier, session_) -> None:
        pass
