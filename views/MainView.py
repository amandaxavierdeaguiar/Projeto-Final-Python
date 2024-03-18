from models.db.db_conection import get_session
from sqlmodel import Session
from customtkinter import *
from PIL import Image
from views.LoginView import LoginView
from views.StockView import StockView


class MainView:
    app: CTk = CTk()
    session: Session = get_session()
    btn_img: CTkImage
    btn_txt: CTkButton
    login: LoginView = LoginView()
    stock: StockView = StockView()

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

        cls.sidebar()
        cls.get_frame()

    @classmethod
    def get_frame(cls):
        # Ainda não esta feito e so para ter qual quer coisa aqui
        is_login = True
        if is_login:
            cls.stock.give_frame(cls.app)
        else:
            cls.login.give_frame(cls.app)

    @classmethod
    def sidebar(cls):
        # Criando Frame do Menu
        sidebar_frame = CTkFrame(master=cls.app, fg_color="#008DD2", width=176, height=650, corner_radius=0)
        sidebar_frame.pack_propagate(0)
        sidebar_frame.pack(fill="y", anchor="w", side="left")

        # logo do menu
        logo_img = Image.open("view/assets/logo-stock.png")
        logo_img = CTkImage(dark_image=logo_img, light_image=logo_img, size=(77.68, 85.42))

        # Colocando e Posicionando a Logo
        CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(48, 0), anchor="center")

        cls.create_button(sidebar_frame, 'view/assets/list.png', 'Login')
        cls.create_button(sidebar_frame, 'view/assets/list.png', 'Produtos')
        cls.create_button(sidebar_frame, 'view/assets/list.png', 'Fornecedores')
        cls.create_button(sidebar_frame, 'view/assets/list.png', 'Sair')

    @classmethod
    def create_button(cls, frame_, img_, text_):
        path_img= Image.open(f'{img_}')
        cls.btn_img = CTkImage(
            dark_image=path_img,
            light_image=path_img)
        cls.btn_txt = CTkButton(
            master=frame_,
            image=cls.btn_img,
            text=f'{text_}',
            fg_color="transparent",
            font=("Verdana", 14),
            hover_color="#045A87",
            anchor="w"
        ).pack(
            anchor="center",
            ipady=5, pady=(60, 0))
