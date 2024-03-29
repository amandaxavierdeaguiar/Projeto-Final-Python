import tkinter as tk

import ttkbootstrap as ttk
from sqlmodel import Session
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from controllers.StockController import StockController
from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session
from views.Product.RegistrationProduct import RegistrationProduct


class StockView(ttk.Frame):
    root = None
    ctrl_stock: StockController = StockController()
    reg_product: RegistrationProduct
    user: UserAuthentication
    session: Session = get_session()
    main_frame: ttk.Frame
    button_add: tk.Button
    dt: Tableview

    def __init__(self, master_, user_):
        super().__init__(master_, padding=(10, 5))
        self.root = master_

    @classmethod
    def get_frame(cls, user_):
        cls.user = user_
        cls.main_frame = ttk.Frame(cls.root, width=400, height=100)
        cls.main_frame.pack(fill=X)

        container = ttk.Frame(master=cls.main_frame, height=20)
        container.pack(fill=X, expand=NO, pady=5)

        # Title and button
        title = tk.Label(container, text="Stock", font=("Verdana", 20), bg="black")
        title.pack(side="left", anchor="nw", fill=tk.NONE, padx=27, pady=29)

        if "Create" in user_.permissions["Stock"]:
            cls.button_add = tk.Button(
                container,
                font=("Verdana", 10),
                text="+ Produtos",
                bg="blue",
                fg="white",
                command=cls.new_product,
                cursor="hand2",
            )
            cls.button_add.pack(anchor="ne", fill=tk.NONE, padx=27, pady=29)
        else:
            cls.button_add = tk.Button(
                container,
                font=("Verdana", 10),
                text="+ Produtos",
                bg="blue",
                fg="white",
                cursor="hand2",
                state="disabled",
            )
            cls.button_add.pack(anchor="ne", fill=tk.NONE, padx=27, pady=29)
        button_feature = tk.Button(
            container,
            font=("Verdana", 10),
            text="Detalhes",
            bg="blue",
            fg="white",
            cursor="hand2",
            command=cls.select_product,
        )
        button_feature.pack(side=RIGHT, padx=5)
        cls.table()
        return cls.main_frame

    @classmethod
    def table(cls):
        container = ttk.Frame(master=cls.main_frame)
        container.pack(fill=tk.BOTH, expand=YES, pady=5)

        table_data = cls.ctrl_stock.get_all(cls.session)
        coldata = [
            {"text": "Bar Code", "stretch": True},
            {"text": "Produto", "stretch": True},
            {"text": "Marca", "stretch": True},
            {"text": "Categoria", "stretch": True},
            {"text": "Preço", "stretch": True},
            {"text": "Quantidade", "stretch": True},
            {"text": "Descrição", "stretch": True},
            {"text": "Foto", "stretch": True},
            {"text": "Categoria_id", "stretch": True},
            {"text": "Marca_id", "stretch": True},
        ]
        rowdata = []
        for row in table_data:
            rowdata.append(row.values())

        cls.dt = Tableview(
            master=container,
            coldata=coldata,
            rowdata=rowdata,
            autofit=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=("#f1f1f1", None),
            height=32,
            paginated=True,
            pagesize=32,
        )
        cls.dt.pack(fill=tk.BOTH, expand=YES, padx=35, pady=35)

    @classmethod
    def select_product(cls):
        selected_rows = cls.dt.get_rows(selected=True)
        tb_columns = cls.dt.get_columns()
        product = {}
        if len(selected_rows) == 1:
            for row in selected_rows:
                row_values = row.values.copy()
                for f, b in zip(tb_columns, row.values.copy()):
                    product[f.headertext] = b
                cls.reg_product = RegistrationProduct(cls.root, cls.user, product)

    @classmethod
    def new_product(cls):
        RegistrationProduct(cls.root, cls.user)
