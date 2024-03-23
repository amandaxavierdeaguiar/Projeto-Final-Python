import hashlib
from customtkinter import *
from PIL import Image
from models.UserAuthentication import UserAuthentication
from views.MainView import MainView
from pydantic import ValidationError


class LoginView:
    app: CTk = CTk()
    main_frame: CTkFrame
    box_email: CTkEntry
    box_pass: CTkEntry
    btn_login: CTkButton
    login_img: CTkImage
    login_lbl: CTkLabel
    error_txt: str = ""
    main_view: MainView

    def __init__(self):
        super().__init__()
        self.window()
        self.app.mainloop()

    @classmethod
    def window(cls):
        cls.app.geometry("1000x650")
        cls.app.title("Stock")
        cls.app.resizable(width=756, height= 545)

        set_appearance_mode("light")
        
        """cls.app.geometry("856x645")
        cls.app.title("Stock")
        cls.app.resizable(False, False)

        set_appearance_mode("light")"""

        cls.main_frame = cls.create_frame()

    @classmethod
    def create_frame(cls) -> CTkFrame:
        # FRAME GERAL DO LOGIN
        frame = CTkFrame(master=cls.app, width=450, height=550, fg_color="#ffffff")
        frame.pack_propagate(False)
        frame.pack(expand=True, side="right")
                
                       
        # imagem
        # logo do menu
   
        """cls.login_img = Image.open("view/assets/login.png")
        cls.login_img = CTkImage(dark_image=cls.login_img, light_image=cls.login_img, size=(120, 120))

        cls.login_lbl = CTkLabel(master=frame, text="", image=cls.login_img)
        cls.login_lbl.pack(pady=(40, 20), anchor="center")"""
        # Colocando e Posicionando a Logo
        # cls.logo_lbl = CTkLabel(master=frame, text="", image=logo_img)
        # cls.logo_lbl.pack(pady=(20, 0), anchor="center")

        # Mensagem boas vindas - login
        CTkLabel(
            master=frame,
            text="Faça seu Login para continuar.",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Verdana", 24),
        ).pack(anchor="center", pady=30)
        
        
        
        
        """CTkLabel(
            master=frame,
            text="Entre!",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Arial Bold", 24),
        ).pack(anchor="w", pady=(5, 5), padx=(25, 0))"""
        """CTkLabel(
            master=frame,
            text="Sign in to your account",
            text_color="#7E7E7E",
            anchor="w",
            justify="left",
            font=("Arial Bold", 12),
        ).pack(anchor="w", padx=(25, 0))"""

        # Entrada Email
        CTkLabel(
            master=frame,
            text="Email:",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Verdana", 14),
            compound="left",
        ).pack(anchor="w", pady=(5, 0), padx=(25, 0))
        # Entrada para por o email
        cls.box_email = CTkEntry(
            master=frame,
            width=400, #225
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
            font=("Verdana", 14),
            compound="left",
        ).pack(anchor="w", pady=(21, 0), padx=(25, 0))
        cls.box_pass = CTkEntry(
            master=frame,
            width=400,#225
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
            font=("Verdana", 14),
            text_color="#ffffff",
            width=120,
            command=cls.on_press_bt_login,
        )#.pack(anchor="w", pady=(40, 0), padx=(25, 0))
        cls.btn_login.pack(pady=(0), side = "right", padx=25)
        
        # BOTAO CADASTRO
        cls.button_register = CTkButton(
            master=frame, 
            text="Cadastra-se", 
            fg_color="#008DD2",
            hover_color="#045A87",
            font=("Verdana", 14),
            text_color="#ffffff",
            width=120)
        cls.button_register.pack(pady=(0), side = "left", padx=25)
        
        
        # Outro Botao
        """CTkButton(
            master=frame,
            text="Register new User",
            fg_color="#EEEEEE",
            hover_color="#EEEEEE",
            font=("Arial Bold", 9),
            text_color="#045A87",
            width=225,
        ).pack(anchor="w", pady=(20, 0), padx=(25, 0))"""

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
    def hash_password(cls, pwd):
        """Hash a password using SHA-256 algorithm"""
        pwd_bytes = pwd.encode("utf-8")
        hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
        return hashed_pwd
