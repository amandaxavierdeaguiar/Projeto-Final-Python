from customtkinter import *
from CTkTable import CTkTable
from PIL import Image


class LoginView:
    login_app: CTk = CTk()

    def __init__(self):
        super().__init__()
        self.windown()
        self.login_app.mainloop()

    @classmethod
    def windown(cls):
        cls.login_app.geometry("856x645")
        cls.login_app.title("Stock")
        cls.login_app.resizable(0, 0)

        set_appearance_mode("light")

        cls.menu = cls.sidebar()
        cls.login_view = cls.login_view()

    @classmethod
    def sidebar(cls):
        # Criando Frame do Menu
        cls.sidebar_frame = CTkFrame(
            master=cls.login_app,
            fg_color="#008DD2",
            width=176,
            height=650,
            corner_radius=0,
        )
        cls.sidebar_frame.pack_propagate(0)
        cls.sidebar_frame.pack(fill="y", anchor="w", side="left")

        # logo do menu
        cls.logo_img = Image.open("./assets/logo-stock.png")
        cls.logo_img = CTkImage(
            dark_image=cls.logo_img, light_image=cls.logo_img, size=(77.68, 85.42)
        )

        # Colocando e Posicionando a Logo

        CTkLabel(master=cls.sidebar_frame, text="", image=cls.logo_img).pack(
            pady=(48, 0), anchor="center"
        )

        # ========== Menu/Botões =============
        # Botao 1 Home
        cls.home_button = Image.open("./assets/home.png")
        cls.home_img = CTkImage(dark_image=cls.home_button, light_image=cls.home_button)
        # Estilo Texto User
        cls.user_button = CTkButton(
            master=cls.sidebar_frame,
            image=cls.home_img,
            text="Login",
            fg_color="transparent",
            font=("Verdana", 14),
            hover_color="#045A87",
            anchor="w",
        ).pack(anchor="center", ipady=5, pady=(60, 0))

        # Botao 2 Produtos
        cls.product_button = Image.open("./assets/list.png")
        returns_img = CTkImage(
            dark_image=cls.product_button, light_image=cls.product_button
        )
        CTkButton(
            master=cls.sidebar_frame,
            image=returns_img,
            text="Produtos",
            fg_color="transparent",
            font=("Verdana", 14),
            hover_color="#045A87",
            anchor="w",
        ).pack(anchor="center", ipady=5, pady=(16, 0))

        # Botão 3 Stock
        cls.button_stock = Image.open("./assets/product.png")
        cls.stock_img = CTkImage(
            dark_image=cls.button_stock, light_image=cls.button_stock
        )

        CTkButton(
            master=cls.sidebar_frame,
            image=cls.stock_img,
            text="Stock",
            fg_color="transparent",
            font=("Verdana", 14),
            hover_color="#045A87",
            anchor="w",
        ).pack(anchor="center", ipady=5, pady=(16, 0))

        # Botao 4 Fornecedores
        cls.button_supplier = Image.open("./assets/supplier.png")
        cls.supplier_img = CTkImage(
            dark_image=cls.button_supplier, light_image=cls.button_supplier
        )
        CTkButton(
            master=cls.sidebar_frame,
            image=cls.supplier_img,
            text="Fornecedores",
            fg_color="transparent",
            font=("Verdana", 14),
            hover_color="#045A87",
            anchor="w",
        ).pack(anchor="center", ipady=5, pady=(16, 0))

        # Button 5 - Sair
        cls.exit_button = Image.open("./assets/exit.png")
        cls.exit_img = CTkImage(dark_image=cls.exit_button, light_image=cls.exit_button)
        CTkButton(
            master=cls.sidebar_frame,
            image=cls.exit_img,
            text="Sair",
            fg_color="transparent",
            font=("Verdana", 14),
            hover_color="#045A87",
            anchor="w",
        ).pack(anchor="center", ipady=5, pady=(16, 0))

        # Botao 6 Login
        cls.login_button = Image.open("./assets/user.png")
        cls.login_img = CTkImage(
            dark_image=cls.login_button, light_image=cls.login_button
        )
        CTkButton(
            master=cls.sidebar_frame,
            image=cls.login_img,
            text="Login",
            fg_color="transparent",
            font=("Verdana", 14),
            hover_color="#045A87",
            anchor="w",
        ).pack(anchor="center", ipady=5, pady=(160, 0))

    @classmethod
    def login_view(cls):

        frame = CTkFrame(
            master=cls.login_app, width=300, height=480, fg_color="#ffffff"
        )
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        # imagem
        # logo do menu
        cls.logo_img = Image.open("./assets/login.png")
        cls.logo_img = CTkImage(
            dark_image=cls.logo_img, light_image=cls.logo_img, size=(77.68, 85.42)
        )

        # Colocando e Posicionando a Logo

        CTkLabel(master=frame, text="", image=cls.logo_img).pack(
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
        cls.txt_email = CTkLabel(
            master=frame,
            text="Email:",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            compound="left",
        ).pack(anchor="w", pady=(5, 0), padx=(25, 0))
        # Entrada para por o email
        cls.email_entry = CTkEntry(
            master=frame,
            width=225,
            fg_color="#EEEEEE",
            border_color="#045A87",
            border_width=1,
            text_color="#000000",
        ).pack(anchor="w", padx=(25, 0))

        # Entrada para por a password
        cls.txt_pass = CTkLabel(
            master=frame,
            text="Password:",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            compound="left",
        ).pack(anchor="w", pady=(21, 0), padx=(25, 0))
        cls.pass_entry = CTkEntry(
            master=frame,
            width=225,
            fg_color="#EEEEEE",
            border_color="#045A87",
            border_width=1,
            text_color="#000000",
            show="*",
        ).pack(anchor="w", padx=(25, 0))

        # Botao Login

        cls.button_login_e = CTkButton(
            master=frame,
            text="Login",
            fg_color="#008DD2",
            hover_color="#045A87",
            font=("Arial Bold", 12),
            text_color="#ffffff",
            width=225,
        ).pack(anchor="w", pady=(40, 0), padx=(25, 0))

        # Outro Botao
        """cls.button_ext = CTkButton(master=frame, text="Continue With Google", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9), text_color="#045A87", width=225).pack(anchor="w", pady=(20, 0), padx=(25, 0))"""

        # FAZER VALIDACAO PARA O EMAIL.


if __name__ == "__main__":
    LoginView()
