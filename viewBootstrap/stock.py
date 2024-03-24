import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from sqlmodel import Session
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from controllers.StockController import StockController
from models.db.db_conection import get_session


class ProductController:
    pass


class Nav:
    root = ttk.Window(themename="lumen")
    ctrl_stock: StockController = StockController()
    session: Session = get_session()
    main_frame: tk.Frame

    def __init__(self):
        self.root.title("Stock Management")
        self.root.geometry("1000x650")
        self.root.minsize(width=756, height=545)
        self.frames_nav()
        self.menu()
        self.table()

    @classmethod
    def frames_nav(cls):
        cls.main_frame = ttk.Frame(cls.root, width=176, height=30, style=PRIMARY)
        cls.main_frame.pack(fill=BOTH, side="left", expand=True)

    @classmethod
    def styleMenu(cls, root):
        root.style = Style()
        root.style.configure(
            "My.TButton", cursor="hand2", compound=tk.LEFT, font=("Verdana", 10)
        )

    @classmethod
    def menu(cls):
        # Botao 1 - Logo
        img_logo = Image.open("assets/logo-stock-b.png")
        cls.img_logo = ImageTk.PhotoImage(img_logo.resize((100, 100)))
        cls.button1 = Button(
            cls.main_frame, width=172, height=230, image=cls.img_logo, text=""
        )
        # cls.button1.configure(style= "My.TButton")
        cls.button1.grid(column=0, row=0)

        # botao 2
        img_img2 = Image.open("assets/list.png")
        cls.img_img2 = ImageTk.PhotoImage(img_img2.resize((30, 35)))
        cls.button2 = Button(
            cls.main_frame,
            width=170,
            height=75,
            cursor="hand2",
            image=cls.img_img2,  # Imagem
            compound=tk.LEFT,  # Posição do texto
            text="   Stock",
            font=("Verdana", 12),  # Fonte
        )
        cls.button2.grid(column=0, row=1)

        # botao 3
        img_img3 = Image.open("assets/supplier.png")
        cls.img_img3 = ImageTk.PhotoImage(img_img3.resize((30, 35)))
        cls.button3 = Button(
            cls.main_frame,
            width=170,
            height=75,
            cursor="hand2",
            image=cls.img_img3,  # Imagem
            compound=tk.LEFT,  # Posição do texto
            text=" Fornecedor",
            font=("Verdana", 12),  # Fonte
        )

        cls.button3.grid(column=0, row=2)  # Posiciona o botão no grid

        # botao 4
        img_img4 = Image.open("assets/user.png")
        cls.img_img4 = ImageTk.PhotoImage(img_img4.resize((25, 25)))
        cls.button4 = Button(
            cls.main_frame,
            width=170,
            height=75,
            cursor="hand2",
            image=cls.img_img4,  # Imagem
            compound=tk.LEFT,  # Posição do texto
            text=" Users",
            font=("Verdana", 12),  # Fonte
        )

        cls.button4.grid(column=0, row=4)  # Posiciona o botão no grid

        # botao 5
        cls.button5 = Button(
            cls.main_frame,
            width=13,
            height=75,
            cursor="hand2",
            # image=cls.img_img5,  # Imagem
            compound=tk.LEFT,  # Posição do texto
            text="Logout",
            font=("Verdana", 12),  # Fonte
        )

        cls.button5.grid(column=0, row=5)  # Posiciona o botão no grid

    @classmethod
    def new_products(cls):
        new_products_frame = tk.Frame(cls.root, width=470, height=100, bg="white")
        new_products_frame.pack(fill=X)

        # Title and button
        title = tk.Label(
            new_products_frame, text="Stock", font=("Verdana", 20), bg="white"
        )
        title.grid(row=0, column=0, padx=30, pady=10)

        button_add = tk.Button(
            new_products_frame,
            font=("Verdana", 10),
            text="+ Produtos",
            bg="blue",
            fg="white",
            cursor="hand2",
        )
        button_add.grid(row=0, column=1, padx=500, pady=10, sticky="e")

        return new_products_frame

    @classmethod
    def table(cls):

        cls.new_products()

        coldata = [
            {"text": "Bar Code", "stretch": True},
            {"text": "Produto", "stretch": True},
            {"text": "Marca", "stretch": True},
            {"text": "Categoria", "stretch": True},
            {"text": "Valor", "stretch": True},
            {"text": "Quantidade", "stretch": True},
        ]

        table_data = cls.ctrl_stock.get_all(cls.session)
        header = ["Bar Code", "Product Name", "Brand", "Category", "Price", "Quantity"]
        rowdata = []
        for row in table_data:
            rowdata.append(row.values())

        dt = Tableview(
            master=cls.root,
            coldata=header,
            rowdata=rowdata,
            autofit=True,
            # paginated=True,
            # height=5,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(cls.colors.light, "black"),
            # search_entry = cls.search_entry
        )
        dt.pack(fill=tk.BOTH, expand=YES, padx=35, pady=35)


if __name__ == "__main__":
    inicio = Nav()
    inicio.root.mainloop()
