import tkinter as tk

import ttkbootstrap as ttk
from sqlmodel import Session
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from controllers.StockController import StockController
from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session
from views.Product.ProductView import ProductView


class TableStockView(ttk.Frame):
    root = None
    ctrl_stock: StockController = StockController()
    reg_product: ProductView
    user: UserAuthentication
    session: Session = get_session()
    main_frame: ttk.Frame
    main_note: ttk.Notebook
    button_add: tk.Button
    dt: Tableview

    def __init__(self, master_, user_, note=None):
        super().__init__(master_, padding=(10, 5))
        self.root = master_
        self.main_note = note

    @classmethod
    def get_frame(cls, user_, note=None):
        cls.user = user_
        cls.main_frame = ttk.Frame(cls.root)
        cls.main_frame.pack(fill=BOTH, side="left", expand=True)
        cls.main_note = note

        cls.table(cls.main_note)
        return cls.main_frame, cls.main_note

    @classmethod
    def table(cls, note):
        container = ttk.Frame(master=note)
        container.pack(fill=tk.BOTH, expand=YES)

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
            height=42,
            paginated=True,
            pagesize=42,
        )
        cls.dt.pack(fill=tk.BOTH, expand=YES)
        cls.main_note.add(container, text='Table')

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
        return product
