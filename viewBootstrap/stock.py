import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

class Nav:
    root = ttk.Window(themename="lumen")
    
    def __init__(self):
        self.root.title("Stock Management")
        self.root.geometry('1000x650')
        self.root.minsize(width=756, height= 545)
        self.frames_nav()
        self.menu()
        self.table()
        
    @classmethod  
    def frames_nav(cls):
        cls.main_frame = tk.Frame(cls.root,  width=176, height=30, bg='black') 
        cls.main_frame.pack(fill=BOTH, side='left', expand=False)
    
    @classmethod 
    def styleMenu(cls, root):
        root.style = Style()
        root.style.configure("My.TButton",
                        cursor='hand2', 
                        compound=tk.LEFT, 
                        font=('Verdana', 10))
    
    @classmethod
    def menu(cls):
        
        # Botao 1 - Logo
        img_logo = Image.open("viewBootstrap/assets/logo-stock-b.png")
        cls.img_logo = ImageTk.PhotoImage(img_logo.resize((100, 100)))
        cls.button1 = Button(cls.main_frame, width=172, height=230, image=cls.img_logo, text='')
        #cls.button1.configure(style= "My.TButton")
        cls.button1.grid(column=0, row=0)

        # botao 2
        img_img2 = Image.open("viewBootstrap/assets/list.png")
        cls.img_img2 = ImageTk.PhotoImage(img_img2.resize((30,35)))
        cls.button2 = Button(cls.main_frame,
            width=170,
            height=75,
            cursor='hand2',
            image=cls.img_img2,  # Imagem
            compound=tk.LEFT,  # Posição do texto
            text='   Stock',
            font=('Verdana', 12)  # Fonte
        )
        cls.button2.grid(column=0, row=1)  
        
        # botao 3
        img_img3 = Image.open("./viewBootstrap/assets/supplier.png")
        cls.img_img3 = ImageTk.PhotoImage(img_img3.resize((30,35)))
        cls.button3 = Button(cls.main_frame,
            width=170,
            height=75,
            cursor='hand2',
            image=cls.img_img3,  # Imagem
            compound=tk.LEFT,  # Posição do texto
            text=' Fornecedor',
            font=('Verdana', 12)  # Fonte
        )

        cls.button3.grid(column=0, row=2)  # Posiciona o botão no grid
        
        # botao 4
        img_img4 = Image.open("viewBootstrap/assets/user.png")
        cls.img_img4 = ImageTk.PhotoImage(img_img4.resize((25,25)))
        cls.button4 = Button(cls.main_frame,
            width=170,
            height=75,
            cursor='hand2',
            image=cls.img_img4,  # Imagem
            compound=tk.LEFT,  # Posição do texto
            text=' Login',
            font=('Verdana', 12)  # Fonte
        )

        cls.button4.grid(column=0, row=4)  # Posiciona o botão no grid
        
        # botao 5
        img_img5 = Image.open("viewBootstrap/assets/user.png")
        cls.img_img5 = ImageTk.PhotoImage(img_img5.resize((25,25)))
        cls.button5 = Button(cls.main_frame,
            width=13,
            height=75,
            cursor='hand2',
            #image=cls.img_img5,  # Imagem
            compound=tk.LEFT,  # Posição do texto
            text=' ',
            font=('Verdana', 12)  # Fonte
        )

        cls.button5.grid(column=0, row=5)  # Posiciona o botão no grid

    @classmethod
    def new_products(cls):
        new_products_frame = tk.Frame(cls.root, width=470, height=100, bg='white')
        new_products_frame.pack(fill=X)

        # Title and button
        title = tk.Label(new_products_frame, text="Stock", font=('Verdana', 20), bg='white')
        title.grid(row=0, column=0, padx=30, pady=10)

        button_add = tk.Button(new_products_frame, font=('Verdana', 10),text="+ Produtos", bg='blue', fg='white', cursor='hand2')
        button_add.grid(row=0, column=1, padx=500, pady=10, sticky='e')
        
        return new_products_frame
    
    """@ classmethod
    def table(cls):
        #cls.new_products()
        TableBootstrap()"""
        
    @ classmethod
    def table(cls):
        cls.colors = cls.root.style.colors
        cls.new_products()
        
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
    
        
if __name__ == "__main__":
    inicio = Nav()
    inicio.root.mainloop()
