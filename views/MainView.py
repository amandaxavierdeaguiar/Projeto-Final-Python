import tkinter as tk
from pathlib import Path
from tkinter import *

import ttkbootstrap as ttk
from PIL import ImageTk, Image
from ttkbootstrap.constants import *

from models.UserAuthentication import UserAuthentication
from views.StockView import StockView
from views.SupplierView import SupplierView

PATH = Path(__file__).parent / "assets"


class MainView(ttk.Frame):
    root = None
    error_txt: str = ""
    menu_frame: ttk.Frame
    main_frame: ttk.Frame
    user: UserAuthentication
    stock: StockView
    supplier: SupplierView
    img_logo: ImageTk.PhotoImage
    button1: Button
    button2: Button
    button3: Button
    button4: Button

    def __init__(self, master, user_: UserAuthentication):
        super().__init__(master, padding=(10, 5))
        self.root = master
        self.user = user_
        self.frames_nav()
        self.menu(user_)
        self.stock = StockView(master, user_)
        self.main_frame = self.stock.get_frame(user_)
        self.pack(fill=BOTH, expand=YES)

    @classmethod
    def frames_nav(cls):
        cls.menu_frame = ttk.Frame(cls.root, width=176, height=30, style=PRIMARY)
        cls.menu_frame.pack(fill=BOTH, side="left", expand=False)

    @classmethod
    def create_button(cls, frame_, img_, text_, command_, row_, disabled_) -> Button:
        img_path_temp = Image.open(PATH / img_)
        img_temp = ImageTk.PhotoImage(img_path_temp.resize((30, 35)))
        if disabled_:
            btn_temp = Button(
                master=frame_,
                width=170,
                height=75,
                cursor="hand2",
                image=img_temp,
                compound=tk.LEFT,
                command=command_,
                text=text_,
                state="disabled",
                font=("Verdana", 12),
            )
            btn_temp.grid(column=0, row=row_)
            return btn_temp
        else:
            btn_temp = Button(
                master=frame_,
                width=170,
                height=75,
                cursor="hand2",
                image=img_temp,
                compound=tk.LEFT,
                command=command_,
                text=text_,
                font=("Verdana", 12),
            )
            btn_temp.grid(column=0, row=row_)
            return btn_temp

    @classmethod
    def menu(cls, user_):
        img_logo = Image.open(PATH / "logo-stock-b.png")
        cls.img_logo = ImageTk.PhotoImage(img_logo.resize((100, 100)))
        cls.button1 = Button(
            cls.menu_frame, width=172, height=230, image=cls.img_logo, text=""
        )
        cls.button1.grid(column=0, row=0)

        cls.button2 = cls.create_button(
            cls.menu_frame, "list.png", "Stock", cls.call_stock, 1, False
        )
        cls.button3 = cls.create_button(
            cls.menu_frame, "supplier.png", "Fornecedor", cls.call_supplier, 2, False
        )

        if "Read" in user_.permissions["Users"]:
            cls.button4 = cls.create_button(
                cls.menu_frame, "user.png", "Users", cls.call_supplier, 3, False
            )
        else:
            cls.button4 = cls.create_button(
                cls.menu_frame, "user.png", "Users", cls.call_supplier, 3, True
            )

        cls.button5 = cls.create_button(
            cls.menu_frame, "exit.png", "Logout", cls.call_exit, 5, False
        )

    @classmethod
    def logout(cls):
        cls.menu_frame.forget()
        # cls.login.window()

    @classmethod
    def call_stock(cls):
        cls.menu_frame.forget()
        cls.stock = StockView(cls.root, cls.user)
        cls.menu_frame = cls.stock.get_frame()

    @classmethod
    def call_supplier(cls):
        cls.menu_frame.forget()
        cls.supplier = SupplierView(cls.root, cls.user)
        # cls.main_frame = cls.supplier.get_frame()

    @classmethod
    def call_exit(cls):
        cls.menu_frame.destroy()
