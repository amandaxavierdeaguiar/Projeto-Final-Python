from customtkinter import *
from PIL import Image

class Menu:    
    def __init__(self):
        #Criando Frame do Menu
        """self.sidebar_frame = CTkFrame(master=self.app, fg_color="#008DD2",  width=176, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")"""
        
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
        