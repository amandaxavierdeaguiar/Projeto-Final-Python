import tkinter as tk
from pathlib import Path
from tkinter import *

import ttkbootstrap as ttk
from PIL import ImageTk, Image
from ttkbootstrap.constants import *

from models.UserAuthentication import UserAuthentication
from views.Login.LoginView import LoginView
from views.Product.ProductView import ProductView
from views.Product.TableStockView import TableStockView
from views.Product.TableStockView import TableStockView
from views.Supplier.SupplierView import SupplierView
from views.Supplier.TableSupplierView import TableSupplierView
from views.User.TableUserView import TableUserView
from views.User.UserView import UserView

PATH = Path(__file__).parent / "assets"


class MainView(ttk.Frame):
    root = None
    user: UserAuthentication
    menu_frame: ttk.Frame
    main_frame: ttk.Frame
    title_frame: ttk.Frame
    stock_tbl: TableStockView
    supplier_tbl: TableSupplierView
    users_tbl: TableUserView
    stock: ProductView
    supplier: SupplierView
    users: UserView
    img_logo: ImageTk.PhotoImage
    button_add: tk.Button
    button_detail: tk.Button
    button1: Button
    button2: Button
    button3: Button
    button4: Button
    button5: Button
    title_var: ttk.StringVar
    title_button_var: ttk.StringVar
    main_note: ttk.Notebook

    def __init__(self, master, user_: UserAuthentication = None):
        super().__init__(master, padding=(0, 0))
        self.root = master
        self.user = user_
        self.title_var = ttk.StringVar(value="Stock")
        self.title_button_var = ttk.StringVar(value="+ Product")
        try:
            login = LoginView(master)
            self.root.wait_window(login.login_frame)
            self.user = login.user
        finally:
            self.if_not_login(title=self.title_var.get(), variavel_add=self.call_stock_add,
                              variavel_update=self.call_stock_update)

    def if_not_login(self, title, variavel_add, variavel_update):
        self.main_frame, self.menu_frame, self.title_frame, self.main_note = self.create_frames()
        self.menu()
        self.title_main(title_=title, variavel_add=variavel_add,
                        variavel_update=variavel_update)
        # self.pack(fill=BOTH, expand=YES)
        ttk.Style("cosmo").configure("TButton", font="TkFixedFont 12")

    def create_frames(self):
        self.menu_frame = ttk.Frame(self.root, width=50, height=30, style=PRIMARY)
        self.menu_frame.pack(fill=Y, side="left", expand=False)
        self.title_frame = ttk.Frame(master=self.root, height=10, padding=(40, 20))
        self.title_frame.pack(fill=X, side="top", expand=False)
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill=BOTH, side="left", expand=True)
        self.main_note = ttk.Notebook(self.main_frame, padding=20)
        self.main_note.pack(fill=BOTH, side="left", expand=True)
        self.stock_tbl = TableStockView(self.root, self.user, self.main_note)
        self.main_frame, self.main_note = self.stock_tbl.get_frame(self.user, self.main_note)
        # self.main_frame.pack(fill=BOTH, side="left", expand=True)
        return self.main_frame, self.menu_frame, self.title_frame, self.main_note

    def menu(self):
        img_logo = Image.open(PATH / "icons/logo-stock-b.png")
        self.img_logo = ImageTk.PhotoImage(img_logo.resize((100, 100)))
        self.button1 = Button(
            self.menu_frame,
            width=150,  # 172
            height=250,
            image=self.img_logo,
            text="",
        )
        self.button1.grid(column=0, row=0)

        self.button2 = self.create_button(
            self.menu_frame, "icons/list.png", "Stock", self.call_stock_tbl, 1, False
        )
        self.button3 = self.create_button(
            self.menu_frame,
            "icons/supplier.png",
            "Fornecedor",
            self.call_supplier_tbl,
            2,
            False,
        )

        if "Read" in self.user.permissions["User"]:
            self.button4 = self.create_button(
                self.menu_frame, "icons/user.png", "Users", self.call_user_tbl, 3, False
            )
        else:
            self.button4 = self.create_button(
                self.menu_frame, "icons/user.png", "Users", self.call_user_tbl, 3, True
            )

        self.button5 = self.create_button(
            self.menu_frame, "icons/exit.png", "Logout", self.call_logout, 5, False
        )

    def title_main(self, title_, variavel_add, variavel_update):
        # Title and button
        title = tk.Label(self.title_frame, font=("Verdana", 20), textvariable=self.title_var)
        title.pack(side="left", padx=10)

        if "Create" in self.user.permissions[f"{title_}"]:
            self.button_add = tk.Button(
                self.title_frame,
                font=("Verdana", 10),
                text=f"+ ",  # Produtos
                bg="blue",
                fg="white",
                command=variavel_add,
                cursor="hand2",
                textvariable=self.title_button_var
            )
            self.button_add.pack(side=RIGHT, padx=15)
        else:
            self.button_add = tk.Button(
                self.title_frame,
                font=("Verdana", 10),
                text=f"+ ",
                bg="blue",
                fg="white",
                cursor="hand2",
                state="disabled",
                textvariable=self.title_button_var
            )
            self.button_add.pack(side=RIGHT, padx=5)
        button_feature = tk.Button(
            self.title_frame,
            font=("Verdana", 10),
            text="Detalhes",
            bg="blue",
            fg="white",
            cursor="hand2",
            command=variavel_update,
        )
        button_feature.pack(side=RIGHT, padx=5)

    @classmethod
    def create_button(cls, frame_, img_, text_, command_, row_, disabled_) -> Button:
        img_path_temp = Image.open(PATH / img_)
        img_temp = ImageTk.PhotoImage(img_path_temp.resize((10, 10)))  # (30, 35)
        if disabled_:
            btn_temp = ttk.Button(
                master=frame_,
                width=20,  # 30
                cursor="hand2",
                image=img_temp,
                compound=tk.LEFT,
                command=command_,
                text=text_,
                state="disabled",
            )
            btn_temp.grid(column=0, row=row_)
            return btn_temp
        else:
            btn_temp = ttk.Button(
                master=frame_,
                width=20,  # 30
                # height=75,
                image=img_temp,
                compound=tk.LEFT,
                command=command_,
                text=text_,
                default="normal",
                state="normal",
                style="my.TButton",
            )
            btn_temp.grid(column=0, row=row_)
            return btn_temp

    def call_logout(self):
        self.main_frame.forget()
        self.menu_frame.forget()
        self.title_frame.forget()
        login = LoginView(self.root)
        self.root.wait_window(login.login_frame)
        self.if_not_login(title="Stock", variavel_add=self.call_stock_add,
                          variavel_update=self.call_stock_update)

    def call_stock_tbl(self):
        self.main_frame.forget()
        self.title_var.set("Stock")
        self.title_button_var.set("+ Product")
        self.stock_tbl = TableStockView(self.root, self.user, self.main_note)
        self.main_frame, self.main_note = self.stock_tbl.get_frame(self.user)

    def call_supplier_tbl(self):
        self.main_frame.forget()
        self.title_var.set("Supplier")
        self.title_button_var.set("+ Supplier")
        self.supplier_tbl = TableSupplierView(self.root, self.user)
        self.main_frame = self.supplier_tbl.get_frame(self.user)

    def call_user_tbl(self):
        self.main_frame.forget()
        self.title_var.set("User")
        self.title_button_var.set("+ User")
        self.users_tbl = TableUserView(self.root, self.user)
        self.main_frame = self.users_tbl.get_frame(self.user)

    def call_stock_update(self):
        seleted = self.stock_tbl.select_product()
        self.stock = ProductView(self.root, self.main_note, self.user, "update", seleted)
        container = self.stock.get_frame(self.main_note, self.user, "update", seleted['Foto'], seleted)
        self.main_note.add(child=container, text="New Product")
        self.main_note.select(1)

    def call_stock_add(self):
        self.stock = ProductView(self.root, self.main_note, self.user, "add")
        container = self.stock.get_frame(self.main_note, self.user, "add")
        self.main_note.add(child=container, text="New Product")
        self.main_note.select(1)

    def call_supplier_update(self):
        seleted = self.supplier_tbl.select_supplier()
        self.supplier = SupplierView(self.root, self.user, seleted)
        self.main_frame = self.supplier.get_frame(self.user)
        self.main_note.select(1)

    def call_supplier_add(self):
        self.main_frame.forget()
        self.title_frame.forget()
        self.supplier = SupplierView(self.root, self.user)
        self.main_frame = self.supplier.get_frame(self.user)

    def call_user_update(self):
        seleted = self.users_tbl.select_user()
        self.main_frame.forget()
        self.title_frame.forget()
        self.users = UserView(self.root, self.user, seleted)
        self.main_frame = self.users_tbl.get_frame(self.user)

    def call_user_add(self):
        self.main_frame.forget()
        self.title_frame.forget()
        self.users = UserView(self.root, self.user)
        self.main_frame = self.users_tbl.get_frame(self.user)
