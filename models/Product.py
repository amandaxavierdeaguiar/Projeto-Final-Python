from typing import Optional
from sqlmodel import Field, SQLModel


# from models.Supplier import Supplier
# from models.Category import Category
# from models.Stock import Stocks


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bar_cod: str = Field(unique=True)
    name: str = Field(unique=True)
    photo: str
    description: str
    price: float
    brand_id: int = Field(default=None, foreign_key="brand.id")
    category_id: int = Field(default=None, foreign_key="category.id")
    # category: Optional[Category] = Relationship(back_populates="category")
    # stocks: List['Stocks'] = Relationship(back_populates="product") #Ver como vai ficar no banco
    """
        Ligaçao ao stocks fica no stocks

        Podemos deixar supplier aqui ou criar class Brand onde nela e que tem o supplier e aqui temos o brand_id    
    """

    @classmethod
    def create(cls, bar_code_, name_, photo_, description_, price_, brand_id_, category_id_):
        cls.bar_cod = bar_code_
        cls.name = name_
        cls.photo = photo_
        cls.description = description_
        cls.price = price_
        cls.brand_id = brand_id_
        cls.category_id = category_id_
        return cls
