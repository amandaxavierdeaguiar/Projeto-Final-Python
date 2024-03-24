import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from sqlmodel import Session
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from controllers.StockController import StockController
from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session


class StockView(ttk.Frame):
    root = None
    ctrl_stock: StockController = StockController()
    user: UserAuthentication
    session: Session = get_session()
    main_frame: tk.Frame
    dt: Tableview

    def __init__(self, master_, user_):
        super().__init__(master_, padding=(10, 5))
        self.root = master_
        self.user = user_

    @classmethod
    def styleMenu(cls, root):
        root.style = Style()
        root.style.configure(
            "My.TButton", cursor="hand2", compound=tk.LEFT, font=("Verdana", 10)
        )

    @classmethod
    def get_frame(cls, user_):
        cls.main_frame = tk.Frame(cls.root, width=400, height=100, bg="white")
        cls.main_frame.pack(fill=X)

        # Title and button
        title = tk.Label(cls.main_frame, text="Stock", font=("Verdana", 20), bg="white")
        title.pack(side="left", anchor="nw", fill=tk.NONE, padx=27, pady=29)

        if "Create" in user_.permissions["Stock"]:
            button_add = tk.Button(
                cls.main_frame,
                font=("Verdana", 10),
                text="+ Produtos",
                bg="blue",
                fg="white",
                cursor="hand2",
            )
            button_add.pack(anchor="ne", fill=tk.NONE, padx=27, pady=29)
        else:
            button_add = tk.Button(
                cls.main_frame,
                font=("Verdana", 10),
                text="+ Produtos",
                bg="blue",
                fg="white",
                cursor="hand2",
                state="disabled",
            )
            button_add.pack(anchor="ne", fill=tk.NONE, padx=27, pady=29)
        cls.table()
        return cls.main_frame

    @classmethod
    def table(cls):
        coldata = [
            {"text": "Bar Code", "stretch": True},
            {"text": "Produto", "stretch": True},
            {"text": "Marca", "stretch": True},
            {"text": "Categoria", "stretch": True},
            {"text": "Valor", "stretch": True},
            {"text": "Quantidade", "stretch": True},
        ]
        table_data = cls.ctrl_stock.get_all(cls.session)
        rowdata = []
        for row in table_data:
            rowdata.append(row.values())

        dt = Tableview(
            master=cls.root,
            coldata=coldata,
            rowdata=rowdata,
            autofit=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=("#f1f1f1", None),
        )
        dt.pack(fill=tk.BOTH, expand=YES, padx=35, pady=35)

        # TEST

    @classmethod
    def select_product(cls):
        selected_rows = cls.dt.get_rows(selected=True)
        if selected_rows == 1:
            for row in selected_rows:
                print(row.values)
