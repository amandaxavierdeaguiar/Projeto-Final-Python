from typing import Optional

from sqlmodel import Field, SQLModel


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    """ 
        Penso nao precisar da lista de produtos a qual estão assossiados porque isso
        e obtido pelo um select
    
        Após ver melhor sobre isso do Relationship ja entedi e pode ser adicionado isso
     
        Isto se a lista não for algo interno ao SQLModel e por isso e que precisa de estar 
    """
