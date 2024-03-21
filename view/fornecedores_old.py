from customtkinter import *
import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel
from PIL import Image
#from description_old import AppDescription

class AppCreateSupplier:
    #see_product: AppDescription =  AppDescription()
    #ctrl_product: ProductController = ProductController
    #()
    app_create_supplier: CTk = CTk()
    #session: Session = get_session()
    
    def __init__(self):
        super().__init__()
        
        self.windown_supplier_create()
        self.description_frames_supplier()
        self.create_supplier_info()
        self.create_supplier()
        self.app_create_supplier.mainloop()
        
        
    @classmethod
    def windown_supplier_create(cls): 
        cls.app_create_supplier.geometry("1000x650")
        cls.app_create_supplier.title("Cadastrar Fornecedor")
        cls.app_create_supplier.minsize(width=756, height= 545)
        set_appearance_mode("light")
        
    
    @ classmethod 
    def description_frames_supplier(cls) -> CTkFrame:         
        #FRAME DE DIVISÃO DA TELA
        cls.prod_frame = ctk.CTkFrame(
            cls.app_create_supplier, 
            width=350, 
            height=650, 
            fg_color="white")
        cls.prod_frame.pack_propagate(0)
        cls.prod_frame.pack(fill="y", anchor="w", side="left")
        #cls.prod_frame.place(relwidth=0.7, relheight=1)
        
        # FRAME PARA POR A FOTO
        cls.photo_bd_frame = CTkFrame(
            master=cls.prod_frame, 
            fg_color="#045A87", 
            width=350, 
            height=350)
        cls.photo_bd_frame.pack_propagate(0)
        cls.photo_bd_frame.place(relwidth=1, relheight=1)
        
        # FRAME PARA DESCRIÇÃO FUNDO
        cls.desc_frame = ctk.CTkFrame(
            cls.app_create_supplier, 
            width=1400, 
            fg_color="#E1E1E1")
        cls.desc_frame.pack_propagate(0)
        cls.desc_frame.pack(fill="y", anchor="w", side="right")
        
        # FRAME PARA POR AS DESCRIÇOES 
        cls.desc_frame_uni = ctk.CTkFrame(
            cls.desc_frame, 
            width=900, #800
            height=600, #600
            fg_color="#E1E1E1") 
        cls.desc_frame_uni.pack_propagate(0)
        cls.desc_frame_uni.pack(anchor="center", pady=150)
        
        # FRAME TITULO PAGINA DESCRIÇÃO
        cls.frame_name = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.frame_name.pack(fill="y", pady=20)
        
        # FRAME TABELA NOME
        cls.frame_name_description = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.frame_name_description.pack(fill="y", pady=10)
        
        # FRAME TABELA ENDEREÇO
        cls.frame_address = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.frame_address.pack(fill="y", pady=10)
        
        # FRAME TABELA TELEFONE
        cls.frame_phone_description = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.frame_phone_description.pack(fill="y", pady=10)
        
        # FRAME PARA O EMAIL
        cls.frame_email_description = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.frame_email_description.pack(fill="y", pady=10)
        
        """# FRAME TABELA DESCRIÇÃO
        cls.frame_des_description = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.frame_des_description.pack(fill="y", pady=10)
        
        # FRAME TABELA CATEGORIA
        cls.frame_category_description = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.frame_category_description.pack(fill="y", pady=10)"""
        
        # FRAME BOTÃO ENVIAR DADOS
        cls.button_frame = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.button_frame.pack(fill="y", pady=20)
   
    @classmethod
    def create_supplier_info(cls):
        
        # COLOCANDO A IMAGEM
        cls.prod_img = Image.open("view/assets/fornecedor.png") # PEGAR NO BANCO DE DADOS
        cls.prod_img = ctk.CTkImage(
            light_image=cls.prod_img, 
            size=(200, 200))
        
        # COLOCANDO E POSICIONANDO A IMAGEM
        
        cls.prod_img_label = ctk.CTkLabel(master=cls.photo_bd_frame, 
                text="", 
                image = cls.prod_img) 
        cls.prod_img_label.place(relwidth=1, relheight=1) #centralizando a imagem
          
    @classmethod   
    def create_supplier(cls):
        
        # INSERIR DADOS DO PRODUTO.
        cls.text_description= "Insira os Dados do Fornecedor:"
        
        # PRINTAR O TITULO DA DESCRIÇÃO
        cls.tit_desc = CTkLabel(
            master= cls.frame_name,
            text= cls.text_description, 
            font= ("Verdana", 20, "bold"),
            text_color="#045A87")
        cls.tit_desc.pack(anchor="center")

        # CAMPO: NOME
        cls.name = CTkLabel(
            master=cls.frame_name_description, 
            text =  "Nome:       ", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.name.pack(fill="x", anchor="n", pady=(0), side= LEFT)
        
      
        # ENTRY PARA BD DO NOME 
        cls.frame_name_ = CTkEntry(cls.frame_name_description,
                                 fg_color="white",  
                                 width=500, 
                                 height=30, 
                                 corner_radius=0)
        cls.frame_name_.pack_propagate(0)
        cls.frame_name_.pack(fill="y", anchor="n", pady=(0), padx= (0), side=RIGHT) #COMMAND
        
    
        # CAMPO: ENDEREÇO
        cls.address_label = CTkLabel(
            cls.frame_address, 
            text =  "Endereço:  ", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.address_label.pack(anchor="n", pady=(0), side= LEFT)

        # ENTRY: CODIGO DE BARRAS
        cls.entry_address = CTkEntry(cls.frame_address,
                                   fg_color="white",  
                                   width=500, 
                                   height=30,
                                   corner_radius=0)
        cls.entry_address.pack(fill="y", anchor="n", pady=(0), padx= (0), side=RIGHT)
        
        # CAMPO: TELEFONE
        cls.label_phone = CTkLabel(
            cls.frame_phone_description, 
            text =  "Telefone:   ",
            text_color= "black", 
            font=("Verdana", 14))
        cls.label_phone.pack(anchor="n", pady=(0), side= LEFT)
        
        # ENTRY: TELEFONE
        cls.entry_phone = CTkEntry(cls.frame_phone_description,
                                   fg_color="white",  
                                   width=500, 
                                   height=30,
                                   corner_radius=0)
        cls.entry_phone.pack(fill="y", anchor="n", pady=(0), padx= (0), side=RIGHT)
                       
        # CAMPO: EMAIL
        cls.label_email = CTkLabel(
            cls.frame_email_description, 
            text =  "E-mail:      ",
            text_color= "black", 
            font=("Verdana", 14))
        cls.label_email.pack(anchor="n", pady=(0), side= LEFT)
        
        # ENTRY PARA EMAIL
        cls.entry_email = CTkEntry(
            cls.frame_email_description,
            fg_color="white",  
            width=500, 
            height=30,
            corner_radius=0)
        cls.entry_email.pack(fill="y", anchor="n", pady=(0), padx= (0), side=RIGHT)
         
        
        # BOTÃO ENVIAR DADOS
        cls.button_prod = CTkButton(master=cls.button_frame, 
                                    fg_color="#008DD2",
                                    text="Guardar informação", 
                                    font=("Verdana", 12), 
                                    text_color="#000000",
                                    border_color= "#E1E1E1", 
                                    #command= cls.open_description  
                                    )
        cls.button_prod.pack(pady=(0), anchor="n")
        
            
            
if __name__ == '__main__':
    AppCreateSupplier()   