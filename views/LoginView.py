import hashlib

from customtkinter import *
from PIL import Image
from sqlmodel import Session

from controllers.UserController import UserController
from models.User import User
from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session
from views.MainView import MainView
from pydantic import ValidationError


class LoginView:
    app: CTk = CTk()
    ctrl_user: UserController = UserController()
    session: Session = get_session()
    main_frame: CTkFrame
    box_email: CTkEntry
    box_pass: CTkEntry
    btn_login: CTkButton
    logo_lbl: CTkLabel
    error_txt: str = ""
    main_view: MainView

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

        cls.main_frame = cls.create_frame()

    @classmethod
    def create_frame(cls) -> CTkFrame:
        frame = CTkFrame(master=cls.app, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(False)
        frame.pack(expand=True, side="right")

        # logo do menu
        logo_img = Image.open("view/assets/login.png")
        logo_img = CTkImage(
            dark_image=logo_img, light_image=logo_img, size=(77.68, 85.42)
        )

        # Colocando e Posicionando a Logo
        # cls.logo_lbl = CTkLabel(master=frame, text="", image=logo_img)
        # cls.logo_lbl.pack(pady=(20, 0), anchor="center")

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
            command=cls.create_user,
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
                cls.app.destroy()
                cls.main_view = MainView(u)
                cls.main_view.window(u)
        except ValidationError as e:
            cls.error_txt = e

    @classmethod
    def create_user(cls):
        u = User()
        u.password = cls.hash_password("123456")
        u.login = "user@email.com"
        u.name = "user"
        cls.ctrl_user.add(u, cls.session)

    @classmethod
    def hash_password(cls, pwd):
        """Hash a password using SHA-256 algorithm"""
        pwd_bytes = pwd.encode("utf-8")
        hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
        return hashed_pwd
