from customtkinter import *
import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel
from PIL import Image
import tkinter as tk

class AppDescription:
    #ctrl: ProductController = ProductController()
    app_description: CTk = CTk()
    #session: Session = get_session()
    
    def __init__(self):
        super().__init__()
        
        self.windown()
        self.img_products()
        self.description_products()
        self.app_description.mainloop()
        
    @classmethod
    def windown(cls): 
        cls.app_description.geometry("756x345") #756x545
        cls.app_description.title("Informações") #Titulo página.
        cls.app_description.resizable(0,0)

        set_appearance_mode("light")
        
    @ classmethod    
    def img_products(cls):
        cls.prod_frame = CTkFrame(master=cls.app_description, fg_color="white",  width=350, height=650, corner_radius=0)
        cls.prod_frame.pack_propagate(0)
        cls.prod_frame.pack(fill="y", anchor="w", side="left")
        
        #logo do menu
        cls.prod_img = Image.open("view/assets/prod1.png")
        cls.prod_img = CTkImage(dark_image=cls.prod_img, light_image=cls.prod_img, size=(250, 250))
        
        # Colocando e Posicionando a Logo
        label = CTkLabel(master=cls.prod_frame, text="", image=cls.prod_img)
        label.pack(pady=(50, 0), anchor="center")
        
    @classmethod   
    def description_products(cls):
        cls.desc_frame = CTkFrame(master=cls.app_description, fg_color="#E1E1E1",  width=450, height=650, corner_radius=0)
        cls.desc_frame.pack_propagate(0)
        cls.desc_frame.pack(fill="y", anchor="w", side="left")
        
        #Titulo Produto
        # Colocando e Posicionando a Logo
        cls.tit_desc = CTkLabel(master=cls.desc_frame, text="Copo de vinho", font=("Verdana", 20, "bold"), text_color="#045A87")
        cls.tit_desc.pack(pady=(30, 0), anchor="center")
        
        #Descricao
        cls.details_label = CTkLabel(cls.desc_frame, text="Dina, 47 cl, 6 unidades\nDesconto de quantidade\nOferta\n• Marca: METRO Professional\n• Capacidade: 47 cl\n• Forma clássica\n• Lavável na máquina de lavar louça\n• Altura: 21.9 cm\n• Conjunto composto por 6 copos",justify="left", font=("Verdana", 14))
        cls.details_label.pack(pady=(30, 0),anchor="center")
        
        # Button Maiores informacoes
        cls.button_prod = CTkButton(master=cls.desc_frame, text="Mais informações", font=("Verdana", 12, "bold"), text_color="white")
        cls.button_prod.pack(pady=(30, 5), anchor="center")
        
        
        
if __name__ == '__main__':
    AppDescription()   