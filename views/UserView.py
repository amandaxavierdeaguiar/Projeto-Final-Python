import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from controllers.UserController import UserController
from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session
from sqlmodel import Session
from customtkinter import *


class UserView(ttk.Frame):
    root = None
    ctrl_user: UserController = UserController()
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
        cls.main_frame = ttk.Frame(cls.root, width=400, height=100)
        cls.main_frame.pack(fill=X)

        container = ttk.Frame(master=cls.main_frame, height=20)
        container.pack(fill=X, expand=NO, pady=5)

        # Title and button
        title = tk.Label(
            container, text="Fornecedores", font=("Verdana", 20), bg="white"
        )
        title.pack(side="left", anchor="nw", fill=tk.NONE, padx=27, pady=29)

        if "Create" in user_.permissions["User"]:
            button_add = tk.Button(
                container,
                font=("Verdana", 10),
                text="+ Fornecedor",
                bg="blue",
                fg="white",
                cursor="hand2",
            )
            button_add.pack(anchor="ne", fill=tk.NONE, padx=27, pady=29)
        else:
            button_add = tk.Button(
                container,
                font=("Verdana", 10),
                text="+ Fornecedor",
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
        container = ttk.Frame(master=cls.main_frame)
        container.pack(fill=tk.BOTH, expand=YES, pady=5)
        coldata = [
            {"text": "Nome", "stretch": True},
            {"text": "Email", "stretch": True},
            {"text": "Tipo de Acesso", "stretch": True},
        ]
        table_data = cls.ctrl_user.get_all(cls.session)
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
        dt.pack(fill=tk.BOTH, expand=YES, padx=35, pady=35)

        # TEST

    @classmethod
    def select_product(cls):
        selected_rows = cls.dt.get_rows(selected=True)
        if selected_rows == 1:
            for row in selected_rows:
                print(row.values)
