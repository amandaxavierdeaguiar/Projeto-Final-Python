from sqlmodel import select

from models.Brand import Brand
from models.Repository.BaseRepository import BaseRepository


class BrandRepository(BaseRepository[Brand]):
    def __init__(self):
        super().__init__()

    def add(self, entity: Brand, session_) -> None:
        pass

    @classmethod
    def get_all(cls, session_):
        statement = select(Brand.name)
        result = session_.exec(statement).all()
        return result

    @classmethod
    def get_by_id(cls, entity: Brand, session_) -> Brand:
        pass

    @classmethod
    def get_by_name(cls, name_: str, session_) -> Brand:
        statement = select(Brand).where(Brand.name == name_)
        result = session_.exec(statement)
        return result

    @classmethod
    def update(cls, entity: Brand, session_) -> None:
        pass

    @classmethod
    def delete(cls, entity: Brand, session_) -> None:
        pass
