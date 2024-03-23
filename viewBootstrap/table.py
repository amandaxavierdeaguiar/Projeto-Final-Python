from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
import ttkbootstrap as ttk
from ttkbootstrap import Style


class TableBootstrap():
    root = ttk.Window(themename="lumen")

    def __init__(self):
        self.colors = self.root.style.colors
        
    @classmethod    
    def table(cls):
        coldata = [
            {"text": "Produto", "stretch": True},
            {"text": "Marca", "stretch": True},
            {"text": "Valor", "stretch": False},
            {"text": "Categoria", "stretch": True},
        ]

        rowdata = [
            ('Alho Poro', 'Marca Propria', 2.98, 'Legume'),
            ('Maçã', 'Fazenda Orgânica', 1.50, 'Fruta'),
            ('Arroz Integral', 'Grãos Saudáveis', 3.75, 'Cereal'),
            ('Iogurte Natural', 'Laticínios Deliciosos', 2.20, 'Laticínio'),
            ('Pão Integral', 'Padaria da Vila', 2.50, 'Pão'),
            ('Queijo Cheddar', 'Queijos Finos', 4.80, 'Laticínio'),
            ('Cenoura', 'Horta da Vovó', 1.25, 'Legume'),
            ('Salmão Fresco', 'Peixaria do Mar', 9.99, 'Peixe'),
            ('Aveia em Flocos', 'Cereais Naturais', 2.30, 'Cereal'),
            ('Mel', 'Apiário da Montanha', 5.00, 'Condimento'),
            ('Espinafre', 'Verduras Frescas', 1.80, 'Legume'),
            ('Leite de Amêndoa', 'Bebidas Alternativas', 3.50, 'Bebida'),
            ('Banana', 'Frutas Tropicais', 0.80, 'Fruta'),
            ('Feijão Preto', 'Leguminosas', 1.70, 'Legume'),
            ('Azeite de Oliva', 'Óleos Premium', 6.50, 'Condimento'),
            ('Abacate', 'Frutas Exóticas', 2.75, 'Fruta'),
            ('Lentilhas', 'Leguminosas', 1.40, 'Legume'),
            ('Chá Verde', 'Bebidas Naturais', 2.00, 'Bebida'),
            ('Tomate', 'Horta da Vovó', 1.10, 'Legume'),
            ('Sardinha Enlatada', 'Conservas do Mar', 1.90, 'Peixe'),
            ('Amêndoas', 'Frutos Secos', 4.50, 'Lanche'),
            ('Batata Doce', 'Horta da Vila', 1.60, 'Legume'),
            ('Iogurte Grego', 'Laticínios Deliciosos', 2.80, 'Laticínio'),
            ('Cebola', 'Horta da Vovó', 1.00, 'Legume'),
            ('Quinoa', 'Grãos Saudáveis', 4.20, 'Cereal'),
            ('Morango', 'Frutas Vermelhas', 3.25, 'Fruta'),
            ('Pasta de Amendoim', 'Lanches Saudáveis', 3.70, 'Lanche'),
            ('Brócolis', 'Verduras Frescas', 1.50, 'Legume'),
            ('Vinho Tinto', 'Bebidas Finas', 12.99, 'Bebida'),
            ('Melancia', 'Frutas Refrescantes', 2.00, 'Fruta'),
            ('kiwi', 'Frutas Citrica', 2.00, 'Fruta'),
        ]
        
        
        dt = Tableview(
            master=cls.root,
            coldata=coldata,
            rowdata=rowdata,
            #paginated=True,
            #height=5,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(cls.colors.light, 'black'),
            #search_entry = cls.search_entry
            )
        dt.pack(fill=BOTH, expand=YES, padx=35, pady=35)    
    
        return Tableview
    