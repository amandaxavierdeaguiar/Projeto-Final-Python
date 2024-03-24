from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
from tkinter import messagebox


class RegisterView:
    register_app: CTk = CTk()

    def __init__(self):
        super().__init__()

        self.window_register()
        self.register_app.mainloop()

    @classmethod
    def window_register(cls):
        cls.register_app.geometry("1000x650")
        cls.register_app.title("Registro")
        cls.register_app.minsize(width=756, height=545)

        set_appearance_mode("light")

        cls.menu = cls.sidebar()
        cls.register_view = cls.register_view()

    @classmethod
    def sidebar(cls):
        # Criando Frame do Menu
        cls.sidebar_frame = CTkFrame(
            master=cls.register_app,
            fg_color="#008DD2",
            width=176,  # 176
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
    def register_view(cls):

        frame = CTkFrame(
            master=cls.register_app, width=450, height=550, fg_color="#ffffff"
        )
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        # MENSAGEM PARA REGISTRAR
        CTkLabel(
            master=frame,
            text="Faça seu cadastro",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Verdana", 24),
        ).pack(anchor="center", pady=30)

        # LABEL NOME:
        cls.txt_name = CTkLabel(
            master=frame,
            text="Nome Completo:",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Verdana", 14),
            compound="left",
        ).pack(anchor="w", pady=(5, 0), padx=(25, 0))

        # ENTRY NOME:
        cls.name_entry = CTkEntry(
            master=frame,
            width=400,
            fg_color="#EEEEEE",
            border_color="#045A87",
            border_width=1,
            text_color="#000000",
        ).pack(anchor="w", padx=(25, 0))

        # LABEL E-MAIL:
        cls.txt_email = CTkLabel(
            master=frame,
            text="Email:",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Verdana", 14),
            compound="left",
        ).pack(anchor="w", pady=(20, 0), padx=(25, 0))

        # ENTRY PARA E-MAIL:
        cls.email_entry = CTkEntry(
            master=frame,
            width=400,
            fg_color="#EEEEEE",
            border_color="#045A87",
            border_width=1,
            text_color="#000000",
        ).pack(anchor="w", padx=(25, 0))

        # LABEL PARA PASSWORD
        cls.txt_pass = CTkLabel(
            master=frame,
            text="Password:",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Verdana", 14),
            compound="left",
        ).pack(anchor="w", pady=(20, 0), padx=(25, 0))

        # ENTRY PARA PASSWORD
        cls.pass_entry = CTkEntry(
            master=frame,
            width=400,
            fg_color="#EEEEEE",
            border_color="#045A87",
            border_width=1,
            text_color="#000000",
            show="*",
        ).pack(anchor="w", padx=(25, 0))

        # LABEL PARA PASSWORD VERIFICACÃO
        cls.txt_pass_verification = CTkLabel(
            master=frame,
            text="Password:",
            text_color="#045A87",
            anchor="w",
            justify="left",
            font=("Verdana", 14),
            compound="left",
        ).pack(anchor="w", pady=(20, 0), padx=(25, 0))

        # ENTRY PARA PASSWORD VERIFICACÃO
        cls.pass_verification_entry = CTkEntry(
            master=frame,
            width=400,
            fg_color="#EEEEEE",
            border_color="#045A87",
            border_width=1,
            text_color="#000000",
            show="*",
        ).pack(anchor="w", padx=(25, 0))

        # BOTAO CADASTRO
        cls.button_register = CTkButton(
            master=frame,
            text="Cadastra-se",
            fg_color="#008DD2",
            hover_color="#045A87",
            font=("Verdana", 14),
            text_color="#ffffff",
            command=cls.cadastrar,
            width=120,
        )
        cls.button_register.pack(pady=(0), side="left", padx=25)

        # BOTAO LOGIN
        cls.button_login_e = CTkButton(
            master=frame,
            text="Login",
            fg_color="#008DD2",
            hover_color="#045A87",
            font=("Verdana", 14),
            text_color="#ffffff",
            width=120,
        ).pack(pady=(0), side="right", padx=25)

    @classmethod
    def cadastrar(cls):
        pass
        """cls.name = cls.name_entry.get()
        cls.email = cls.email_entry.get()
        cls.password = cls.pass_entry.get()
        cls.confirm_password = cls.pass_verification_entry.get()

        if cls.name == '' or cls.email == '' or cls.password == '' or cls.confirm_password == '':
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
        elif cls.password  != cls.confirm_password:
            messagebox.showerror("Erro", "As senhas não conferem")
        else:
            # Código para cadastrar o cliente no banco de dados ou em algum sistema

            """

    @classmethod
    def validar_email(cls, email):
        if "@" in email and "." in email:
            return True
        return False


if __name__ == "__main__":
    RegisterView()
