from models.Repository.SupplierRepository import SupplierRepository
from models.Supplier import Supplier


class SupplierController:
    def __init__(self):
        pass

    @classmethod
    def add(cls):
        cnt = SupplierRepository()
        s = Supplier('Empresa1', 'TesteEndEmpresa1', '987654', 'empresa1@empresa')
        cnt.add(s)
        # cnt.update(s)
