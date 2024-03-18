from customtkinter import *
from CTkTable import CTkTable
from PIL import Image

class Stock:
    def __init__(self):
        super().__init__()

        self.app = CTk()
        self.app.geometry("856x645")
        self.app.title("Stock")
        self.app.resizable(0,0)

        set_appearance_mode("light")
        
        self.menu = sidebar(self)
        self.stock = stock(self)
        
def sidebar(self):
    #Criando Frame do Menu
    self.sidebar_frame = CTkFrame(master=self.app, fg_color="#008DD2",  width=176, height=650, corner_radius=0)
    self.sidebar_frame.pack_propagate(0)
    self.sidebar_frame.pack(fill="y", anchor="w", side="left")
    
    #logo do menu
    self.logo_img = Image.open("view/assets/logo-stock.png")
    self.logo_img = CTkImage(dark_image=self.logo_img, light_image=self.logo_img, size=(77.68, 85.42))
    
    # Colocando e Posicionando a Logo
    
    CTkLabel(master=self.sidebar_frame, text="", image=self.logo_img).pack(pady=(48, 0), anchor="center")
    
    # ========== Menu/Botões =============
    # Botao 1 Home
    self.home_button = Image.open("view/assets/home.png")
    self.home_img = CTkImage(dark_image=self.home_button, light_image=self.home_button)
    #Estilo Texto User 
    self.user_button = CTkButton(master=self.sidebar_frame, image=self.home_img, text="Login", fg_color="transparent", font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))
    
    # Botao 2 Produtos
    self.product_button = Image.open("view/assets/list.png")
    returns_img = CTkImage(dark_image=self.product_button, light_image=self.product_button)
    CTkButton(master=self.sidebar_frame, image=returns_img, text="Produtos", fg_color="transparent", font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
    
    # Botão 3 Stock  
    self.button_stock = Image.open("view/assets/product.png")
    self.stock_img = CTkImage(dark_image=self.button_stock, light_image=self.button_stock)
    
    CTkButton(master=self.sidebar_frame, image=self.stock_img, text="Stock", fg_color="transparent", font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
    
    # Botao 4 Fornecedores 
    self.button_supplier = Image.open("view/assets/supplier.png")
    self.supplier_img = CTkImage(dark_image=self.button_supplier, light_image=self.button_supplier)
    CTkButton(master=self.sidebar_frame, image=self.supplier_img, text="Fornecedores", fg_color="transparent", font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
    
    # Button 5 - Sair
    self.exit_button = Image.open("view/assets/exit.png")
    self.exit_img = CTkImage(dark_image=self.exit_button, light_image=self.exit_button)
    CTkButton(master=self.sidebar_frame, image=self.exit_img, text="Sair", fg_color="transparent", font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))
      
    # Botao 6 Login
    self.login_button = Image.open("view/assets/user.png")
    self.login_img = CTkImage(dark_image=self.login_button, light_image=self.login_button)
    CTkButton(master=self.sidebar_frame, image=self.login_img, text="Login", fg_color="transparent", font=("Verdana", 14), hover_color="#045A87", anchor="w").pack(anchor="center", ipady=5, pady=(160, 0))

def stock(self):
    #Criando espaço para por a tela do Stock
    self.main_view = CTkFrame(master=self.app, fg_color="#fff",  width=680, height=650, corner_radius=0)
    self.main_view.pack_propagate(0)
    self.main_view.pack(side="left")

    title_frame = CTkFrame(master=self.main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))
    
    #=========== TITULO STOCK ===========
    #Titulo
    CTkLabel(master=title_frame, text="Stock", font=("Verdana", 30), text_color="#045A87").pack(anchor="nw", side="left")
    
    # Add novos produtos
    CTkButton(master=title_frame, text="+ Novos Produtos",  font=("Verdana", 15), text_color="#fff", fg_color="#008DD2", hover_color="#045A87", cursor= 'hand2').pack(anchor="ne", side="right")
    
    # Botão Pesquisar produto
    search_container = CTkFrame(master=self.main_view, height=50, fg_color="#A9DCF6")
    search_container.pack(fill="x", pady=(45, 0), padx=27)
    
    # Botao pesquisa de produto
    CTkEntry(master=search_container, width=305, placeholder_text="Pesquise o produto", border_color="#008DD2", border_width=2).pack(side="left", padx=(13, 0), pady=15)
    
    #Pesquisar por data 
    self.box_date = CTkComboBox(master=search_container,
                width=125, 
                values=["Date", "Data Recentes", "Data antigas"], 
                button_color="#008DD2", #Botao Ordem Data
                border_color="#008DD2", 
                border_width=2, 
                button_hover_color="#045A87", #Botao data  hover
                dropdown_hover_color="#045A87", # Dentro 
                dropdown_fg_color="#008DD2", 
                dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
    self.box_status = CTkComboBox(master=search_container, 
                width=125, 
                values=["Pesquisar:", "Nome", "ID", "Descrição", "Fornecedor"], button_color="#008DD2",
                border_color="#008DD2",
                border_width=2,
                button_hover_color="#045A87",
                dropdown_hover_color="#045A87",
                dropdown_fg_color="#008DD2",
                dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
    
    #PRODUTOS(IMPORTAR DA DATABASE)

    self.table_data = [
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
    
    self.table_frame = CTkScrollableFrame(master=self.main_view, fg_color="transparent")
    self.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
    self.table = CTkTable(master=self.table_frame, values=self.table_data, colors=["#E6E6E6", "#EEEEEE"], header_color="#008DD2", hover_color="#B4B4B4")
    self.table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
    self.table.pack(expand=True)

if  __name__ == "__main__":
    inicio = Stock()
    inicio.app.mainloop()
    Stock()
