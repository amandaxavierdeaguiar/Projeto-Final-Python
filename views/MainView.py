import tkinter as tk
from pathlib import Path
from tkinter import *

import ttkbootstrap as ttk
from PIL import ImageTk, Image
from ttkbootstrap.constants import *

from models.UserAuthentication import UserAuthentication
from views.Product.StockView import StockView
from views.Supplier.SupplierView import SupplierView
from views.User.UserView import UserView

PATH = Path(__file__).parent / "assets"


class MainView(ttk.Frame):
    root = None
    user: UserAuthentication
    menu_frame: ttk.Frame
    main_frame: ttk.Frame
    stock: StockView
    supplier: SupplierView
    users: UserView
    img_logo: ImageTk.PhotoImage
    button1: Button
    button2: Button
    button3: Button
    button4: Button
    button5: Button

    def __init__(self, master, user_: UserAuthentication):
        super().__init__(master, padding=(10, 5))
        self.root = master
        self.user = user_
        self.frames_nav()
        self.menu()
        # self.pack(fill=BOTH, expand=YES)
        ttk.Style("cosmo").configure("TButton", font="TkFixedFont 12")

    def frames_nav(self):
        self.menu_frame = ttk.Frame(self.root, width=50, height=30, style=PRIMARY)
        self.menu_frame.pack(fill=Y, side="left", expand=False)
        self.stock = StockView(self.root, self.user)
        self.main_frame = self.stock.get_frame(self.user)
        self.main_frame.pack(fill=BOTH, side="left", expand=True)

    @classmethod
    def create_button(cls, frame_, img_, text_, command_, row_, disabled_) -> Button:
        img_path_temp = Image.open(PATH / img_)
        img_temp = ImageTk.PhotoImage(img_path_temp.resize((30, 35)))
        if disabled_:
            btn_temp = ttk.Button(
                master=frame_,
                width=30,
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
                width=25,
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
            width=172,
            height=230,
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
                self.menu_frame, "icons/user.png", "Users", self.call_user, 3, False
            )
        else:
            self.button4 = self.create_button(
                self.menu_frame, "icons/user.png", "Users", self.call_user, 3, True
            )

        self.button5 = self.create_button(
            self.menu_frame, "icons/exit.png", "Logout", self.call_logout, 5, False
        )

    def call_logout(self):
        self.destroy()

    def call_stock(self):
        self.main_frame.destroy()
        self.stock = StockView(self.root, self.user)
        self.main_frame = self.stock.get_frame(self.user)

    def call_supplier(self):
        self.main_frame.destroy()
        self.supplier = SupplierView(self.root, self.user)
        self.main_frame = self.supplier.get_frame(self.user)

    def call_user(self):
        self.main_frame.destroy()
        self.users = UserView(self.root, self.user)
        self.main_frame = self.users.get_frame(self.user)
