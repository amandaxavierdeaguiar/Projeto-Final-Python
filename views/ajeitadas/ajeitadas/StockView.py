import tkinter as tk
import ttkbootstrap as ttk
from sqlmodel import Session
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap import Style

from controllers.StockController import StockController
from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session


class StockView(ttk.Frame):
    root = None
    ctrl_stock: StockController = StockController()
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
        #cls.main_frame = ttk.Frame(cls.root, width=400, height=100)
        cls.main_frame = ttk.Frame(cls.root, width=400, height=10)
        cls.main_frame.pack(fill=X)

        container = ttk.Frame(master=cls.main_frame, height=10)
        container.pack(fill=X, expand=YES, pady=5)

        # Title and button
        title = tk.Label(container, text="Stock", font=("Verdana", 20)) #bg="black"
               
        title.pack(side="left", padx=10)  #(side="left", anchor="nw", fill=tk.NONE, padx=27, pady=29)
        
        if "Create" in user_.permissions["Stock"]:
            button_add = tk.Button(
                container,
                font=("Verdana", 10),
                text="+ Produtos",
                bg="blue",
                fg="white",
                cursor="hand2",
            )
            button_add.pack(side=RIGHT, padx=15) #5
        else:
            button_add = tk.Button(
                container,
                font=("Verdana", 10),
                text="+ Produtos",
                bg="blue",
                fg="white",
                cursor="hand2",
                state="disabled",
            )
            button_add.pack(side=RIGHT, padx=5)
            
        button_feature = tk.Button(container,
                font=("Verdana", 10),
                text="Detalhes",
                bg="blue",
                fg="white",
                cursor="hand2",)
        button_feature.pack(side=RIGHT, padx=5)
        
        cls.table()
        return cls.main_frame

    @classmethod
    def table(cls):
        container = ttk.Frame(master=cls.main_frame)
        container.pack(fill=tk.BOTH, expand=YES, pady=5)

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
        dt.pack(fill=tk.BOTH, expand=YES, padx=10, pady=0)

        # TEST

    @classmethod
    def select_product(cls):
        selected_rows = cls.dt.get_rows(selected=True)
        if selected_rows == 1:
            for row in selected_rows:
                print(row.values)
