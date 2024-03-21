import asyncio
import hashlib

from customtkinter import *
from PIL import Image

from models.UserAuthentication import UserAuthentication
from views.LoginView import LoginView
from views.MenuView import MenuView
from views.StockView import StockView
from views.SupplierView import SupplierView
from pydantic import ValidationError


class MainView:
    app: CTk = CTk()
    btn_products: CTkButton
    btn_supplier: CTkButton
    btn_login: CTkButton
    btn_exit: CTkButton
    main_frame: CTkFrame
    menu_frame: CTkFrame
    box_email: CTkEntry
    box_pass: CTkEntry
    btn_login: CTkButton
    error_txt: str = ""
    login: LoginView = LoginView(app)
    stock: StockView = StockView()
    supplier: SupplierView = SupplierView()
    menu: MenuView = MenuView()

    def __init__(self):
        super().__init__()
        self.window()
        self.app.mainloop()

    @classmethod
    def window(cls):
        cls.app.geometry("856x645")
        cls.app.title("Stock")
        cls.app.resizable(False, False)

        set_appearance_mode("light")

        cls.menu_frame = cls.menu.sidebar(cls.app)

        cls.create_buttons_menu()
        cls.main_frame = cls.give_login_frame()

    @classmethod
    def create_buttons_menu(cls):
        # Criaçao dos botoes do menu
        cls.btn_products = cls.menu.create_button(
            cls.menu_frame, "view/assets/product.png", "Produtos", cls.call_stock
        )
        cls.btn_supplier = cls.menu.create_button(
            cls.menu_frame, "view/assets/supplier.png", "Supplier", cls.call_supplier
        )
        cls.btn_exit = cls.menu.create_button(
            cls.menu_frame, "view/assets/exit.png", "Sair", cls.call_exit
        )

    @classmethod
    def give_login_frame(cls) -> CTkFrame:
        frame = CTkFrame(master=cls.app, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(False)
        frame.pack(expand=True, side="right")

        # logo do menu
        logo_img = Image.open("view/assets/login.png")
        logo_img = CTkImage(
            dark_image=logo_img, light_image=logo_img, size=(77.68, 85.42)
        )

        # Colocando e Posicionando a Logo

        CTkLabel(master=frame, text="", image=logo_img).pack(
            pady=(20, 0), anchor="center"
        )

        # Mensagem boas vindas - login
        CTkLabel(
            master=frame,
            text="Entre!",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Arial Bold", 24),
        ).pack(anchor="w", pady=(5, 5), padx=(25, 0))
        CTkLabel(
            master=frame,
            text="Sign in to your account",
            text_color="#7E7E7E",
            anchor="w",
            justify="left",
            font=("Arial Bold", 12),
        ).pack(anchor="w", padx=(25, 0))

        # Entrada Email
        CTkLabel(
            master=frame,
            text="Email:",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            compound="left",
        ).pack(anchor="w", pady=(5, 0), padx=(25, 0))
        # Entrada para por o email
        cls.box_email = CTkEntry(
            master=frame,
            width=225,
            fg_color="#EEEEEE",
            border_color="#045A87",
            border_width=1,
            text_color="#000000",
        )
        cls.box_email.pack(anchor="w", padx=(25, 0))

        # Entrada para por a password
        CTkLabel(
            master=frame,
            text="Password:",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            compound="left",
        ).pack(anchor="w", pady=(21, 0), padx=(25, 0))
        cls.box_pass = CTkEntry(
            master=frame,
            width=225,
            fg_color="#EEEEEE",
            border_color="#045A87",
            border_width=1,
            text_color="#000000",
            show="*",
        )
        cls.box_pass.pack(anchor="w", padx=(25, 0))

        # Botao Login
        cls.btn_login = CTkButton(
            master=frame,
            text="Login",
            fg_color="#008DD2",
            hover_color="#045A87",
            font=("Arial Bold", 12),
            text_color="#ffffff",
            width=225,
            command=cls.on_press_bt_login,
        ).pack(anchor="w", pady=(40, 0), padx=(25, 0))

        # Outro Botao
        CTkButton(
            master=frame,
            text="Register new User",
            fg_color="#EEEEEE",
            hover_color="#EEEEEE",
            font=("Arial Bold", 9),
            text_color="#045A87",
            width=225,
        ).pack(anchor="w", pady=(20, 0), padx=(25, 0))

        CTkLabel(
            master=frame,
            text=f"{cls.error_txt}",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            compound="left",
        ).pack(anchor="w", pady=(22, 0), padx=(25, 0))
        return frame

    @classmethod
    def on_press_bt_login(cls):
        try:
            email = cls.box_email.get()
            password = cls.hash_password(cls.box_pass.get())
            u = UserAuthentication()
            u.check(email, password)
            if u.is_login:
                return cls.call_stock()
        except ValidationError as e:
            cls.error_txt = e

    @classmethod
    def logout(cls):
        pass

    @classmethod
    def call_stock(cls):
        cls.main_frame.forget()
        cls.main_frame = cls.stock.get_frame()

    @classmethod
    def call_login(cls):
        cls.main_frame.forget()
        cls.main_frame = cls.login.give_frame(cls.app)

    @classmethod
    def call_supplier(cls):
        cls.main_frame.forget()
        cls.main_frame = cls.supplier.give_frame(cls.app)

    @classmethod
    def call_exit(cls):
        cls.main_frame.forget()
        cls.main_frame = cls.login.give_frame(cls.app)

    @classmethod
    def hash_password(cls, pwd):
        """Hash a password using SHA-256 algorithm"""
        pwd_bytes = pwd.encode("utf-8")
        hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
        return hashed_pwd
