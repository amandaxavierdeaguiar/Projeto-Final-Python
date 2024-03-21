from customtkinter import *
import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel
from PIL import Image

""" TRANSFORMEI EM RESPONSIVO, POREM AINDA SE ENCONTRA EM DESENVOLVIMENTO! VOU INCLUIR A DESCRIÇÃO DO PRODUTO CONFORME COMBINADO, CLICANDO JA MUDA A TELA. """

class AppDescription:
    #ctrl_product: ProductController = ProductController()
    app_description: CTk = CTk()
    #session: Session = get_session()
    
    def __init__(self):
        super().__init__()
        
        self.window_description()
        self.description_frames()
        self.create_product_info()
        self.description_products()
        self.app_description.mainloop()
        
        
    @classmethod
    def window_description(cls): 
        cls.app_description.geometry("1000x650")
        cls.app_description.title("Editar Produto")
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
        
        """ INCLUIR SO NOS FRAMES """
        # FRAME PARA POR A FOTO NA DESCRIÇÃO DO PRODUTO
        cls.photo_bd_frame = CTkFrame(
            master=cls.prod_frame, 
            fg_color="white", 
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
            width=700, #500 
            height=40, 
            corner_radius=0)
        cls.button_frame.pack(fill="y", pady=00)
        
    
    @classmethod
    def create_product_info(cls):
        
        # COLOCANDO A IMAGEM
        cls.prod_img = Image.open("view/assets/alho_frances.png") # PEGAR NO BANCO DE DADOS
        cls.prod_img = ctk.CTkImage(
            light_image=cls.prod_img, 
            size=(200, 200))
        
        # COLOCANDO E POSICIONANDO A IMAGEM
        
        cls.prod_img_label = ctk.CTkLabel(master=cls.photo_bd_frame, 
                text="", 
                image = cls.prod_img) 
        cls.prod_img_label.place(relwidth=1, relheight=1) #centralizando a imagem
        
    @classmethod   
    def description_products(cls):
        
        # INSERIR DADOS DO PRODUTO.
        cls.text_description= "Descrições do produto:"
        
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
        
      
        # LABLE PARA BD DO NOME 
        cls.text_name = "Alho Francês"
        cls.frame_name_ = CTkLabel(cls.frame_name_description,
                                 fg_color="white",  
                                 width=500, 
                                 height=30, 
                                 text = cls.text_name,
                                 text_color = "black", 
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
        cls.text_cod_bar = "cod_123456789"
        cls.entry_cod_bar = CTkLabel(cls.frame_cod_bar_description,
                                   fg_color="white",  
                                   width=500, 
                                   height=30,
                                   text  = cls.text_cod_bar,
                                   text_color = "black", 
                                   corner_radius=0)
        cls.entry_cod_bar.pack(fill="y", anchor="n", pady=(0), padx= (0), side=RIGHT)
        
        # CAMPO: MARCA
        cls.label_brand = CTkLabel(
            cls.frame_brand_description, 
            text =  "Marca:      ",
            text_color= "black", 
            font=("Verdana", 14))
        cls.label_brand.pack(anchor="n", pady=(0), side= LEFT)
        
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
        
        # LABEL PARA PREÇO
        cls.text_value = 2.78
        cls.entry_value = CTkLabel(
            cls.frame_value_description,
            fg_color="white",  
            width=500, 
            height=30,
            text  = cls.text_value,
            text_color = "black", 
            corner_radius=0)
        cls.entry_value.pack(fill="y", anchor="n", pady=(0), padx= (0), side=RIGHT)
          
        # CAMPO: DESCRIÇÃO
        cls.label_desc = CTkLabel(
            cls.frame_des_description, 
            text =  "Descrição: ", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.label_desc.pack(anchor="n", pady=(0), side= LEFT)
        
        # LABEL: DESCRIÇÃO
        cls.text_description = " Descrição do produto "
        cls.entry_desc = CTkLabel(
            cls.frame_des_description,
            fg_color="white",  
            width=500, 
            height=150,
            text = cls.text_description, 
            text_color="black",
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
        
        # BOTÃO EDITAR PRODUTO
        cls.button_prod = CTkButton(master=cls.button_frame, 
                                    fg_color="#B2B3B3",
                                    text="Guardar produto", 
                                    font=("Verdana", 12), 
                                    text_color="#000000",
                                    border_color= "#E1E1E1"
                                    ) #command=
        #cls.button_prod.pack(pady=(0), anchor="n")
        cls.button_prod.pack(pady=(0), side=LEFT, padx=10)
        
        
        #BOTAO LIXEIRA
        # COLOCANDO A IMAGEM ICON
        cls.prod_img = Image.open("view/assets/lixeira.png") # PEGAR NO BANCO DE DADOS
        cls.prod_img = ctk.CTkImage(
            light_image=cls.prod_img, 
            size=(20, 20))

        cls.button_exclui = CTkButton(master=cls.button_frame, 
                                    fg_color="#B2B3B3",
                                    text="Apagar produto", 
                                    font=("Verdana", 12), 
                                    image= cls.prod_img,
                                    text_color="#000000",
                                    border_color= "#E1E1E1"
                                    ) #command=
        #cls.button_prod.pack(pady=(0), anchor="n")
        cls.button_exclui.pack(pady=(0), side=RIGHT)
                        
        
if __name__ == '__main__':
    AppDescription()   