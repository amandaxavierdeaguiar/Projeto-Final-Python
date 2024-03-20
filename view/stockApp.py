from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
from controllers.StockController import StockController
from models.db.db_conection import get_session
from sqlmodel import Session


class StockView:
    ctrl: StockController = StockController()
    app: CTk = CTk()
    session: Session = get_session()

    def __init__(self):
        super().__init__()
        self.windown()
        self.app.mainloop()

    @classmethod
    def windown(cls):
        cls.app.geometry("856x645")
        cls.app.title("Stock")
        cls.app.resizable(0, 0)

        set_appearance_mode("light")

        cls.menu = cls.sidebar()
        cls.list_stock = cls.list_stock()
        
        cls.app.mainloop()

    @classmethod
    def sidebar(cls):

        # logo do menu
        cls.logo_img = Image.open("view/assets/logo-stock.png")
        cls.logo_img = CTkImage(dark_image=cls.logo_img, light_image=cls.logo_img, size=(77.68, 85.42))

        # Colocando e Posicionando a Logo

        CTkLabel(master=cls.sidebar_frame, text="", image=cls.logo_img).pack(pady=(48, 0),anchor="center")

        # ========== Menu/Botões =============
        # Botao 1 Home
        cls.home_button = Image.open("view/assets/home.png")
        cls.home_img = CTkImage(dark_image=cls.home_button, light_image=cls.home_button)
        # Estilo Texto User
        cls.user_button = CTkButton(master=cls.sidebar_frame, image=cls.home_img, text="Login", fg_color="transparent",font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

        # Botao 2 Produtos
        cls.product_button = Image.open("view/assets/list.png")
        returns_img = CTkImage(dark_image=cls.product_button, light_image=cls.product_button)
        CTkButton(master=cls.sidebar_frame, image=returns_img, text="Produtos", fg_color="transparent",font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

        # Botão 3 Stock  
        cls.button_stock = Image.open("view/assets/product.png")
        cls.stock_img = CTkImage(dark_image=cls.button_stock, light_image=cls.button_stock)

        CTkButton(master=cls.sidebar_frame, image=cls.stock_img, text="Stock", fg_color="transparent",
                  font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

        # Botao 4 Fornecedores 
        cls.button_supplier = Image.open("view/assets/supplier.png")
        cls.supplier_img = CTkImage(dark_image=cls.button_supplier, light_image=cls.button_supplier)
        CTkButton(master=cls.sidebar_frame, image=cls.supplier_img, text="Fornecedores", fg_color="transparent",font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

        # Button 5 - Sair
        cls.exit_button = Image.open("view/assets/exit.png")
        cls.exit_img = CTkImage(dark_image=cls.exit_button, light_image=cls.exit_button)
        CTkButton(master=cls.sidebar_frame, image=cls.exit_img, text="Sair", fg_color="transparent",font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

        # Botao 6 Login
        cls.login_button = Image.open("view/assets/user.png")
        cls.login_img = CTkImage(dark_image=cls.login_button, light_image=cls.login_button)
        CTkButton(master=cls.sidebar_frame, image=cls.login_img, text="Login", fg_color="transparent",font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

    @classmethod
    def list_stock(cls):
        # Criando espaço para por a tela do Stock
        cls.main_view = CTkFrame(master=cls.app, fg_color="#fff", width=680, height=650, corner_radius=0)
        cls.main_view.pack_propagate(0)
        cls.main_view.pack(side="left")

        title_frame = CTkFrame(master=cls.main_view, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        # =========== TITULO STOCK ===========
        # Titulo
        CTkLabel(master=title_frame, text="Stock", font=("Verdana", 30), text_color="#045A87").pack(anchor="nw",side="left")

        # Add novos produtos
        CTkButton(master=title_frame, text="+ Novos Produtos", font=("Verdana", 15), text_color="#fff",
                  fg_color="#008DD2", hover_color="#045A87", cursor='hand2').pack(anchor="ne", side="right")

        # Botão Pesquisar produto
        search_container = CTkFrame(master=cls.main_view, height=50, fg_color="#A9DCF6")
        search_container.pack(fill="x", pady=(45, 0), padx=27)

        # Botao pesquisa de produto
        CTkEntry(master=search_container, width=305, placeholder_text="Pesquise o produto", border_color="#008DD2",
                 border_width=2).pack(side="left", padx=(13, 0), pady=15)

        # Pesquisar por data
        cls.box_date = CTkComboBox(master=search_container,
                                   width=125,
                                   values=["Date", "Data Recentes", "Data antigas"],
                                   button_color="#008DD2",  # Botao Ordem Data
                                   border_color="#008DD2",
                                   border_width=2,
                                   button_hover_color="#045A87",  # Botao data  hover
                                   dropdown_hover_color="#045A87",  # Dentro
                                   dropdown_fg_color="#008DD2",
                                   dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
        cls.box_status = CTkComboBox(master=search_container,
                                     width=125,
                                     values=["Pesquisar:", "Nome", "ID", "Descrição", "Fornecedor"],
                                     button_color="#008DD2",
                                     border_color="#008DD2",
                                     border_width=2,
                                     button_hover_color="#045A87",
                                     dropdown_hover_color="#045A87",
                                     dropdown_fg_color="#008DD2",
                                     dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

        # PRODUTOS(IMPORTAR DA DATABASE)

        # cls.product = cls.table_data()

        cls.table_data = [
            ["Order ID", "Item Name", "Customer", "Address", "Status", "Quantity"],
            ['3833', 'Smartphone', 'Alice', '123 Main St', 'Confirmed', '8'],
            ['6432', 'Laptop', 'Bob', '456 Elm St', 'Packing', '5'],
            ['2180', 'Tablet', 'Crystal', '789 Oak St', 'Delivered', '1'],
            ['5438', 'Headphones', 'John', '101 Pine St', 'Confirmed', '9'],
            ['9144', 'Camera', 'David', '202 Cedar St', 'Processing', '2'],
            ['7689', 'Printer', 'Alice', '303 Maple St', 'Cancelled', '2'],
            ['1323', 'Smartwatch', 'Crystal', '404 Birch St', 'Shipping', '6'],
            ['7391', 'Keyboard', 'John', '505 Redwood St', 'Cancelled', '10'],
            ['4915', 'Monitor', 'Alice', '606 Fir St', 'Shipping', '6'],
            ['5548', 'External Hard Drive', 'David', '707 Oak St', 'Delivered', '10'],
            ['5485', 'Table Lamp', 'Crystal', '808 Pine St', 'Confirmed', '4'],
            ['7764', 'Desk Chair', 'Bob', '909 Cedar St', 'Processing', '9'],
            ['8252', 'Coffee Maker', 'John', '1010 Elm St', 'Confirmed', '6'],
            ['2377', 'Blender', 'David', '1111 Redwood St', 'Shipping', '2'],
            ['5287', 'Toaster', 'Alice', '1212 Maple St', 'Processing', '1'],
            ['7739', 'Microwave', 'Crystal', '1313 Cedar St', 'Confirmed', '8'],
            ['3129', 'Refrigerator', 'John', '1414 Oak St', 'Processing', '5'],
            ['4789', 'Vacuum Cleaner', 'Bob', '1515 Pine St', 'Cancelled', '10']
        ]

        # Definições Tabela

        cls.table_frame = CTkScrollableFrame(master=cls.main_view, fg_color="transparent")
        cls.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        cls.table = CTkTable(master=cls.table_frame, values=cls.table_data, colors=["#E6E6E6", "#EEEEEE"],
                             header_color="#008DD2", hover_color="#B4B4B4")
        cls.table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
        cls.table.pack(expand=True)

    @classmethod
    def table_data(cls):
        return cls.ctrl.get_all(cls.session)

if __name__ == '__main__':
    StockView()