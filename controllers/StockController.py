from models.Repository.StockRepository import StocksRepository
from models.Supplier import Supplier


class StockController:
    def __init__(self):
        pass

    @classmethod
    def add(cls):
        cnt = StocksRepository()
        st = Supplier('Empresa1', 'TesteEndEmpresa1', '987654', 'empresa1@empresa')
        cnt.add(st)
        # cnt.update(st)
