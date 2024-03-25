from sqlmodel import select

from models.Product import Product
from models.Brand import Brand
from models.Category import Category
from models.Repository.BaseRepository import BaseRepository


class ProductRepository(BaseRepository[Product]):
    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Product, session_) -> None:
        session_.add(entity)
        session_.commit()
        session_.refresh(entity)

    @classmethod
    def get_all(cls, session_):
        statement = (
            select(
                Product.bar_cod,
                Product.name,
                Brand.name,
                Category.name,
                Product.price,
                Product.description,
                Product.photo,
            )
            .join(Brand)
            .join(Category)
            .order_by(Product.id)
        )
        result = session_.exec(statement).mappings().alL()
        return result

    @classmethod
    def get_by_id(cls, entity: Product, session_) -> Product:
        statement = select(entity).where(entity.id == entity.id)
        result = session_.exec(statement)
        return result

    @classmethod
    def update(cls, entity: Product, session_) -> None:
        statement = select(entity).where(entity.id == entity.id)
        exec_result = session_.exec(statement)
        result = exec_result.one()

        result = entity
        session_.add(result)
        session_.commit()
        session_.refresh(result)

    @classmethod
    def delete(cls, entity: Product, session_) -> None:
        statement = select(entity).where(entity.id == entity.id)
        exec_result = session_.exec(statement)
        result = exec_result.one()

        session_.delete(result)
        session_.commit()

        statement = select(entity).where(entity.id == entity.id)
        exec_confirm = session_.exec(statement)
        result_confirm = exec_confirm.first()

        if result_confirm is None:
            print("Successfully Deleted")
