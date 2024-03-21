from customtkinter import *
import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel
from PIL import Image

class AppRegisterProduct:
    
    #ctrl_product: ProductController = ProductController()
    app_description: CTk = CTk()
    #session: Session = get_session()
    
    def __init__(self):
        super().__init__()
        
        self.windown_description()
        self.description_frames()
        self.create_product_info()
        self.edition_products()
        self.app_description.mainloop()
        
        
    @classmethod
    def windown_description(cls): 
        cls.app_description.geometry("1000x650")
        cls.app_description.title("Cadastrar Produto")
        cls.app_description.minsize(width=756, height= 545)
        set_appearance_mode("light")
        
    
    @ classmethod 
    def description_frames(cls) -> CTkFrame:
        #NOVA ALTERAÇÃO PARA TORNAR RESPONSIVO!
         
        #FRAME DE DIVISÃO DA TELA
        cls.prod_frame = ctk.CTkFrame(
            cls.app_description, 
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
            cls.app_description, 
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
        cls.desc_frame_uni.pack(anchor="center", pady=50)
        
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
        
        # FRAME TABELA CODIGO BARRAS
        cls.frame_cod_bar_description = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.frame_cod_bar_description.pack(fill="y", pady=10)
        
        # FRAME TABELA MARCA
        cls.frame_brand_description = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.frame_brand_description.pack(fill="y", pady=10)
        
        # FRAME PARA O VALOR
        cls.frame_value_description = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.frame_value_description.pack(fill="y", pady=10)
        
        # FRAME TABELA DESCRIÇÃO
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
        cls.frame_category_description.pack(fill="y", pady=10)
        
        # FRAME BOTÃO ENVIAR DADOS
        cls.button_frame = CTkFrame(master=cls.desc_frame_uni, 
            fg_color="#E1E1E1",  
            width=500, 
            height=40, 
            corner_radius=0)
        cls.button_frame.pack(fill="y", pady=00)
        
    
    @classmethod
    def create_product_info(cls):
        
        # COLOCANDO A IMAGEM
        cls.prod_img = Image.open("view/assets/logo-stock-b.png") # PEGAR NO BANCO DE DADOS
        cls.prod_img = ctk.CTkImage(
            light_image=cls.prod_img, 
            size=(200, 200))
        
        # COLOCANDO E POSICIONANDO A IMAGEM
        
        cls.prod_img_label = ctk.CTkLabel(master=cls.photo_bd_frame, 
                text="", 
                image = cls.prod_img) 
        cls.prod_img_label.place(relwidth=1, relheight=1) #centralizando a imagem
    
        # BOTAO PARA PEDIR PARA INSERIREM IMAGEM NO BANCO DE DADOS  -    FAZER LIGAÇÃO
        cls.button_img = CTkButton(master=cls.photo_bd_frame, 
                                    fg_color="#008DD2",
                                    text="CARREGUE SUA IMAGEM", 
                                    font=("Verdana", 12), 
                                    text_color="#000000",
                                    border_color= "#E1E1E1"
                                    )
        cls.button_img.pack(anchor="center")
        cls.button_img.place(in_=cls.prod_img_label, relx=0.27, rely=0.7) 
        
        #COMMAND
        
    @classmethod   
    def edition_products(cls):
        
        # INSERIR DADOS DO PRODUTO.
        cls.text_description= "Insira os Dados do produto:"
        
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
            text =  "Nome:      ", 
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
        
        # CAMPO: CODIGO DE BARRAS
        cls.label_cod_bar = CTkLabel(
            cls.frame_cod_bar_description, 
            text =  "Codigo:     ", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.label_cod_bar.pack(anchor="n", pady=(0), side= LEFT)

        # ENTRY: CODIGO DE BARRAS
        cls.entry_cod_bar = CTkEntry(cls.frame_cod_bar_description,
                                   fg_color="white",  
                                   width=500, 
                                   height=30,
                                   corner_radius=0)
        cls.entry_cod_bar.pack(fill="y", anchor="n", pady=(0), padx= (0), side=RIGHT)
        
        # CAMPO: MARCA
        cls.label_brand = CTkLabel(
            cls.frame_brand_description, 
            text =  "Marca:      ",
            text_color= "black", 
            font=("Verdana", 14))
        cls.label_brand.pack(anchor="n", pady=(0), side= LEFT)
        
        # ENTRY: MARCA
        # BOX: MARCA
        cls.box_brand= CTkComboBox(cls.frame_brand_description,
                                     values=["Milaneza", "Barilla", "Nacional", "Cigala", "Garofalo", "Bom Petisco", "Baci", "Starbucks", "Kinder" ,"Tritão", "Compal", "Fula", "Lays", "Sidul", "Nobre", "Gallo", "Oliveira da Serra", "Outros"],
                                     button_color="#008DD2",
                                     border_color="#008DD2",
                                     button_hover_color="#008DD2",
                                     dropdown_hover_color="#008DD2",
                                     dropdown_fg_color="#E1E1E1",
                                     dropdown_text_color="#000000",
                                     width=500,
                                     height=30, 
                                     )
        cls.box_brand.pack(fill="y", anchor="n", pady=(0), padx= (0,0), side= RIGHT)
        #expand=True)
               
        # CAMPO: PREÇO
        cls.label_value = CTkLabel(
            cls.frame_value_description, 
            text =  "Preço:       ",
            text_color= "black", 
            font=("Verdana", 14))
        cls.label_value.pack(anchor="n", pady=(0), side= LEFT)
        
        # ENTRY PARA PREÇO
        cls.entry_value = CTkEntry(
            cls.frame_value_description,
            fg_color="white",  
            width=500, 
            height=30,
            corner_radius=0)
        cls.entry_value.pack(fill="y", anchor="n", pady=(0), padx= (0), side=RIGHT)
          
        # CAMPO: DESCRIÇÃO
        cls.label_desc = CTkLabel(
            cls.frame_des_description, 
            text =  "Descrição: ", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.label_desc.pack(anchor="n", pady=(0), side= LEFT)
        
        # ENTRY: DESCRIÇÃO
        cls.entry_desc = CTkEntry(
            cls.frame_des_description,
            fg_color="white",  
            width=500, 
            height=150,
            corner_radius=0)
        cls.entry_desc.pack(fill="y", anchor="n", pady=(0), padx= (0), side=RIGHT)
        
        # CATEGORIA frame_category_description
        cls.category_label = CTkLabel(
            cls.frame_category_description, 
            text =  "Categoria:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.category_label.pack(anchor="n", pady=(0), side= LEFT)
        

        
        cls.box_categoria= CTkComboBox(cls.frame_category_description,
                                     values=["Vegetais", "Fruta", "Verdura", "Açougue", "Não perecíveis", "Peixaria", "Congelados", "Frios", "Bebidas", "Outros"],
                                     button_color="#008DD2",
                                     border_color="#008DD2",
                                     button_hover_color="#008DD2",
                                     dropdown_hover_color="#008DD2",
                                     dropdown_fg_color="#E1E1E1",
                                     dropdown_text_color="#000000",
                                     width=500,
                                     height=30, 
                                     )
        cls.box_categoria.pack(fill="y", anchor="n", pady=(0), padx= (0,0), side= RIGHT)
        #expand=True)
        
        # BOTÃO ENVIAR DADOS
        cls.button_prod = CTkButton(master=cls.button_frame, 
                                    fg_color="#008DD2",
                                    text="Guardar informação", 
                                    font=("Verdana", 12), 
                                    text_color="#000000",
                                    border_color= "#E1E1E1",                    
                                    ) #command= cls.open_description 
        cls.button_prod.pack(pady=(0), anchor="n")
                        
    @classmethod
    def open_description(cls):
        pass
    
    
    
            
if __name__ == '__main__':
    AppRegisterProduct()   