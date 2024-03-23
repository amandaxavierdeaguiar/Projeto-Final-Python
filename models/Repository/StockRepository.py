from sqlmodel import select

from models.Brand import Brand
from models.Category import Category
from models.Product import Product
from models.Repository.BaseRepository import BaseRepository, T
from models.Stock import Stock


class StocksRepository(BaseRepository[Stock]):
    def get_by_id(self, entity: T, session_) -> T:
        pass

    def __init__(self):
        super().__init__()

    @classmethod
    def add(cls, entity: Stock, session_) -> None:
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
                Stock.quantity,
            )
            .join(Brand)
            .join(Category)
            .join(Stock)
            .order_by(Product.id)
        )
        result = session_.exec(statement).all()
        return result

    @classmethod
    def get_by_bar_code(cls, session_, bar_code_):
        statement = (
            select(
                Product.bar_cod,
                Product.name,
                Brand.name,
                Category.name,
                Product.price,
                Stock.quantity,
            )
            .join(Brand)
            .join(Category)
            .join(Stock)
            .where(Product.bar_cod == bar_code_)
            .order_by(Product.id)
        )
        result = session_.exec(statement).all()
        return result

    @classmethod
    def get_by_name(cls, session_, name):
        statement = (
            select(
                Product.bar_cod,
                Product.name,
                Brand.name,
                Category.name,
                Product.price,
                Stock.quantity,
            )
            .join(Brand)
            .join(Category)
            .join(Stock)
            .where(Product.name == name)
            .order_by(Product.id)
        )
        result = session_.exec(statement).all()
        return result

    @classmethod
    def get_all_by_category(cls, session_, category_):
        statement = (
            select(
                Product.bar_cod,
                Product.name,
                Brand.name,
                Category.name,
                Product.price,
                Stock.quantity,
            )
            .join(Brand)
            .join(Category)
            .join(Stock)
            .where(Category.name == category_)
            .order_by(Product.id)
        )
        result = session_.exec(statement).all()
        return result

    @classmethod
    def get_all_by_brand(cls, session_, brand_):
        statement = (
            select(
                Product.bar_cod,
                Product.name,
                Brand.name,
                Category.name,
                Product.price,
                Stock.quantity,
            )
            .join(Brand)
            .join(Category)
            .join(Stock)
            .where(Brand.name == brand_)
            .order_by(Product.id)
        )
        result = session_.exec(statement).all()
        return result

    @classmethod
    def update(cls, entity: Stock, session_) -> None:
        statement = select(entity).where(entity.id == entity.id)
        exec_result = session_.exec(statement)
        result = exec_result.one()

        result = entity
        session_.add(result)
        session_.commit()
        session_.refresh(result)

    @classmethod
    def delete(cls, entity: Stock, session_) -> None:
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
