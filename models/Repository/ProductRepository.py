from http.client import HTTPException

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
        statement = select(Product).where(Product.id == entity.id)
        result = session_.exec(statement)
        return result

    @classmethod
    def update(cls, entity: Product, session_) -> None:
        test = entity.bar_cod
        statement = select(Product).where(Product.bar_cod is entity.bar_cod)
        exec_result = session_.exec(statement)
        list_result = exec_result.all()
        result = [x for x in list_result if x.bar_cod == entity.bar_cod][0]
        result.name = entity.name
        result.bar_cod = entity.bar_cod
        result.description = entity.description
        result.photo = entity.photo
        result.brand_id = entity.brand_id
        result.category_id = entity.category_id
        result.price = entity.price
        session_.add(result)
        session_.commit()
        session_.refresh(result)

    @classmethod
    def delete(cls, entity: Product, session_) -> None:
        statement = select(Product).where(Product.id == entity.id)
        exec_result = session_.exec(statement)
        result = exec_result.one()

        session_.delete(result)
        session_.commit()

        statement = select(Product).where(Product.id == entity.id)
        exec_confirm = session_.exec(statement)
        result_confirm = exec_confirm.first()

        if result_confirm is None:
            print("Successfully Deleted")
