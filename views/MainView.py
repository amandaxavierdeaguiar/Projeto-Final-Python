from customtkinter import *
from PIL import Image

from models.UserAuthentication import UserAuthentication
from views.StockView import StockView
from views.SupplierView import SupplierView


class MainView:
    app: CTk = CTk()
    btn_products: CTkButton
    btn_supplier: CTkButton
    btn_exit: CTkButton
    main_frame: CTkFrame
    menu_frame: CTkFrame
    box_email: CTkEntry
    box_pass: CTkEntry
    btn_login: CTkButton
    error_txt: str = ""
    user: UserAuthentication
    stock: StockView
    supplier: SupplierView

    def __init__(self, user_: UserAuthentication):
        self.user = user_
        super().__init__()

    @classmethod
    def window(cls, user_: UserAuthentication):
        cls.user = user_
        cls.app.geometry("856x645")
        cls.app.title("Stock")
        cls.app.resizable(False, False)

        set_appearance_mode("light")

        cls.menu_frame = cls.sidebar(cls.app)

        cls.create_buttons_menu()
        cls.stock = StockView(cls.app, cls.user)
        cls.main_frame = cls.stock.get_frame()
        cls.app.mainloop()

    @classmethod
    def create_buttons_menu(cls):
        # Criaçao dos botoes do menu
        cls.btn_products = cls.create_button(
            cls.menu_frame, "view/assets/product.png", "Produtos", cls.call_stock
        )
        cls.btn_supplier = cls.create_button(
            cls.menu_frame, "view/assets/supplier.png", "Supplier", cls.call_supplier
        )
        cls.btn_exit = cls.create_button(
            cls.menu_frame, "view/assets/exit.png", "Sair", cls.call_exit
        )

    @classmethod
    def logout(cls):
        cls.main_frame.forget()
        # cls.login.window()

    @classmethod
    def call_stock(cls):
        cls.main_frame.forget()
        cls.stock = StockView(cls.app, cls.user)
        cls.main_frame = cls.stock.get_frame()

    @classmethod
    def call_supplier(cls):
        cls.main_frame.forget()
        cls.supplier = SupplierView(cls.app, cls.user)
        cls.main_frame = cls.supplier.get_frame()

    @classmethod
    def call_exit(cls):
        cls.main_frame.destroy()

    @classmethod
    def create_button(cls, frame_, img_, text_, command_) -> CTkButton:
        path_img = Image.open(f"{img_}")
        btn_img = CTkImage(dark_image=path_img, light_image=path_img)
        btn_temp = CTkButton(
            master=frame_,
            image=btn_img,
            text=f"{text_}",
            fg_color="transparent",
            font=("Verdana", 14),
            hover_color="#045A87",
            anchor="w",
            command=command_,
            state="normal",
        )
        btn_temp.pack(anchor="center", ipady=5, pady=(60, 0))
        return btn_temp

    @classmethod
    def sidebar(cls, app_):
        # Criando Frame do Menu
        menu_frame = CTkFrame(
            master=app_, fg_color="#008DD2", width=176, height=650, corner_radius=0
        )
        menu_frame.pack_propagate(False)
        menu_frame.pack(fill="y", anchor="w", side="left")

        # logo do menu
        logo_img_path = Image.open("view/assets/logo-stock-b.png")
        logo_img = CTkImage(
            dark_image=logo_img_path,
            light_image=logo_img_path,
            size=(77.68, 85.42),
        )

        # Colocando e Posicionando a Logo
        menu_logo = CTkLabel(master=menu_frame, image=logo_img)
        menu_logo.pack(pady=(48, 0), anchor="center")
        return menu_frame
