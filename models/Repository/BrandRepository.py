from models.Brand import Brand
from models.Repository.BaseRepository import BaseRepository


class BrandRepository(BaseRepository[Brand]):
    def __init__(self):
        super().__init__()

    def add(self, entity: Brand, session_) -> None:
        pass

    def get_all(self, session_):
        pass

    def get_by_id(self, entity: Brand, session_) -> Brand:
        pass

    def update(self, entity: Brand, session_) -> None:
        pass

    def delete(self, entity: Brand, session_) -> None:
        pass
