import tkinter as tk
from pathlib import Path
from tkinter import *

import ttkbootstrap as ttk
from PIL import ImageTk, Image
from ttkbootstrap.constants import *

from models.UserAuthentication import UserAuthentication
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
    title_main_lbl: str
    user: UserAuthentication
    menu_frame: ttk.Frame
    main_frame: ttk.Frame
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

    def __init__(self, master, user_: UserAuthentication):
        super().__init__(master, padding=(0, 0))
        # super().__init__(master, padding=(10, 5))
        self.root = master
        self.user = user_
        self.frames_nav()
        self.menu()
        self.title_main(user_=user_, title_="Stock", txt_button="Stock", variavel_=self.call_stock)
        # self.pack(fill=BOTH, expand=YES)
        ttk.Style("cosmo").configure("TButton", font="TkFixedFont 12")

    def frames_nav(self):
        self.menu_frame = ttk.Frame(self.root, width=50, height=30, style=PRIMARY)
        self.menu_frame.pack(fill=Y, side="left", expand=False)
        self.stock_tbl = TableStockView(self.root, self.user)
        self.main_frame = self.stock_tbl.get_frame(self.user)
        self.main_frame.pack(fill=X, side="left", expand=True)
        # self.main_frame.pack(fill=BOTH, side="left", expand=True)

    @classmethod
    def create_button(cls, frame_, img_, text_, command_, row_, disabled_) -> Button:
        img_path_temp = Image.open(PATH / img_)
        img_temp = ImageTk.PhotoImage(img_path_temp.resize((10, 10)))  # (30, 35)
        if disabled_:
            btn_temp = ttk.Button(
                    master=frame_,
                    width=20,  # 30
                    # height=75,
                    cursor="hand2",
                    image=img_temp,
                    compound=tk.LEFT,
                    command=command_,
                    text=text_,
                    state="disabled",
                    # font=("Verdana", 12),
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
                self.menu_frame, "icons/list.png", "Stock", self.call_stock, 1, False
        )
        self.button3 = self.create_button(
                self.menu_frame,
                "icons/supplier.png",
                "Fornecedor",
                self.call_supplier,
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

    @classmethod
    def title_main(cls, user_, title_, txt_button, variavel_):
        # TITULO PRODUTO TABLE
        container = ttk.Frame(master=cls.main_frame, height=10)
        container.pack(fill=X, expand=YES, pady=5)

        # Title and button
        title = tk.Label(container, text=title_, font=("Verdana", 20))
        title.pack(side="left", padx=10)

        if "Create" in user_.permissions[f"{title_}"]:
            cls.button_add = tk.Button(
                    container,
                    font=("Verdana", 10),
                    text=f"+ {txt_button}",  # Produtos
                    bg="blue",
                    fg="white",
                    command=variavel_,
                    cursor="hand2",
            )
            cls.button_add.pack(side=RIGHT, padx=15)
        else:
            cls.button_add = tk.Button(
                    container,
                    font=("Verdana", 10),
                    text="+ {txt_button}",
                    bg="blue",
                    fg="white",
                    cursor="hand2",
                    state="disabled",
            )
            cls.button_add.pack(side=RIGHT, padx=5)
        button_feature = tk.Button(
                container,
                font=("Verdana", 10),
                text="Detalhes",
                bg="blue",
                fg="white",
                cursor="hand2",
                command=variavel_,
        )
        button_feature.pack(side=RIGHT, padx=5)

    def call_logout(self):
        self.destroy()

    def call_stock_tbl(self):
        self.main_frame.destroy()
        self.stock_tbl = TableStockView(self.root, self.user)
        self.main_frame = self.stock_tbl.get_frame(self.user)

    def call_supplier_tbl(self):
        self.main_frame.destroy()
        self.supplier_tbl = TableSupplierView(self.root, self.user)
        self.main_frame = self.supplier_tbl.get_frame(self.user)

    def call_user_tbl(self):
        self.main_frame.destroy()
        self.users_tbl = TableUserView(self.root, self.user)
        self.main_frame = self.users_tbl.get_frame(self.user)

    def call_stock(self):
        self.main_frame.destroy()
        self.stock = ProductView(self.root, self.user)
        self.main_frame = self.stock.get_frame(self.user)

    def call_supplier(self):
        self.main_frame.destroy()
        self.supplier = SupplierView(self.root, self.user)
        self.main_frame = self.supplier.get_frame(self.user)

    def call_user(self):
        self.main_frame.destroy()
        self.users = UserView(self.root, self.user)
        self.main_frame = self.users_tbl.get_frame(self.user)
