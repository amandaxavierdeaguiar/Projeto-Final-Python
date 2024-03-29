import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session
from sqlmodel import Session
from controllers.SupplierController import SupplierController


class TableSupplierView(ttk.Frame):
    root = None
    ctrl_supplier: SupplierController = SupplierController()
    user: UserAuthentication
    session: Session = get_session()
    main_frame: ttk.Frame
    dt: Tableview

    def __init__(self, master_, user_):
        super().__init__(master_, padding=(10, 5))
        self.root = master_
        self.user = user_

    @classmethod
    def get_frame(cls, user_):
        # cls.main_frame = ttk.Frame(cls.root, width=400, height=100)
        cls.main_frame = ttk.Frame(cls.root, width=400, height=10, padding=20)
        cls.main_frame.pack(fill=X)

        cls.table()
        return cls.main_frame

    @classmethod
    def table(cls):
        container = ttk.Frame(master=cls.main_frame)
        container.pack(fill=tk.BOTH, expand=YES)
        coldata = [
            {"text": "Fornecedor", "stretch": True},
            {"text": "Morada", "stretch": True},
            {"text": "Email", "stretch": True},
            {"text": "Telefone", "stretch": True},
        ]
        table_data = cls.ctrl_supplier.get_all(cls.session)
        rowdata = []
        for row in table_data:
            rowdata.append(row.values())

        dt = Tableview(
            master=container,
            coldata=coldata,
            rowdata=rowdata,
            autofit=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=("#f1f1f1", None),
            height=32,
            paginated=True,
        )
        # dt.pack(fill=tk.BOTH, expand=YES, padx=35, pady=35)
        dt.pack(fill=tk.BOTH, expand=YES)

        # TEST

    @classmethod
    def select_supplier(cls):
        selected_rows = cls.dt.get_rows(selected=True)
        tb_columns = cls.dt.get_columns()
        supplier = {}
        if len(selected_rows) == 1:
            for row in selected_rows:
                row_values = row.values.copy()
                for f, b in zip(tb_columns, row.values.copy()):
                    supplier[f.headertext] = b
        return supplier
