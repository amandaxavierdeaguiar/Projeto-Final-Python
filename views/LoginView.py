import hashlib

from models.Enums.TypeAccess import TypeAccess
from models.User import User
from models.db.db_conection import get_session
from controllers.UserController import UserController
from sqlmodel import Session
from customtkinter import *
from PIL import Image


class LoginView:
    ctrl_user: UserController = UserController()
    is_login: bool = False
    session: Session = get_session()
    box_email: CTkEntry
    box_pass: CTkEntry
    error_txt: str = ""

    def __init__(self):
        super().__init__()

    @classmethod
    def give_frame(cls, app_: CTk) -> CTkFrame:
        frame = CTkFrame(master=app_, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        # imagem
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
        CTkButton(
            master=frame,
            text="Login",
            fg_color="#008DD2",
            hover_color="#045A87",
            font=("Arial Bold", 12),
            text_color="#ffffff",
            width=225,
            command=cls.login,
        ).pack(anchor="w", pady=(40, 0), padx=(25, 0))

        # Outro Botao
        CTkButton(
            master=frame,
            text="Continue With Google",
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
    def login(cls):
        email = cls.box_email.get()
        password = cls.hash_password(cls.box_pass.get())
        if not cls.ctrl_user.authenticate_user(email, password, cls.session):
            cls.error_txt = "Incorrect Login or Password."

    @classmethod
    def logout(cls):
        pass

    @classmethod
    def create_user(cls):
        u = User()
        cls.ctrl_user.add(u, cls.session)

    @classmethod
    def hash_password(cls, pwd):
        """Hash a password using SHA-256 algorithm"""
        pwd_bytes = pwd.encode("utf-8")
        hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
        return hashed_pwd
