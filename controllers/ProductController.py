from models.Repository.ProductRepository import ProductRepository
from models.Product import Product

class ProductController():
    def add(self):
        cnt = ProductRepository()
        p = Product('CodigoBarraTeste', 'ProdutoTeste', 'Descricao teste', '234', '45.8')
        cnt.add(p)
        #cnt.update(p)