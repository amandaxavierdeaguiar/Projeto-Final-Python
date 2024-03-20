from customtkinter import *
import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel
from PIL import Image
import tkinter as tk
import customtkinter


class AppEditProduct:
    #ctrl_product: ProductController = ProductController()
    app_description: CTk = CTk()
    #session: Session = get_session()
    
    def __init__(self):
        super().__init__()
        
        self.windown()
        self.description_frame()
        self.edition_products()
        self.app_description.mainloop()
        
    @classmethod
    def windown(cls): 
        cls.app_description.geometry("756x345") #756x545
        cls.app_description.title("Informações") #Titulo página.
        cls.app_description.resizable(0,0)

        set_appearance_mode("light")
    
    @ classmethod 
    def description_frame(cls) -> CTkFrame:
        #Frame para dividir a tela na parte esquerda.
        cls.prod_frame = CTkFrame(
            cls.app_description, 
            fg_color="white",  
            width=350, 
            height=650, 
            corner_radius=0)
        cls.prod_frame.pack_propagate(0)
        cls.prod_frame.pack(fill="y", anchor="w", side="left")
        
        # Frame para por a foto
        cls.photo_bd_frame = CTkFrame(
            master=cls.prod_frame, 
            fg_color="white",  
            width=350, 
            height=350, 
            corner_radius=0)
        cls.photo_bd_frame.pack_propagate(0)
        cls.photo_bd_frame.pack(anchor="center")
        
        #INSERINDO IMAGEM PARA TESTAR BANCO DE DADOS.
        
        cls.prod_img = Image.open("view/assets/logo-stock.png")
        cls.prod_img = CTkImage(light_image=cls.prod_img, 
                                size=(150, 150))
        cls.prod_img_label = CTkLabel(
            master=cls.photo_bd_frame, 
            text="", 
            image=cls.prod_img)
        cls.prod_img_label.pack(pady=(50, 0), anchor="center")
        
        
        #BOTAO AO INVES IMAGEM
        cls.button_img = CTkButton(master=cls.photo_bd_frame, 
                                    fg_color="#008DD2",
                                    text="CARREGUE SUA IMAGEM", 
                                    font=("Verdana", 12), 
                                    text_color="#000000",
                                    border_color= "#E1E1E1")
        cls.button_img.pack(pady=(40), anchor="center")
        
        
        
        
        
        
        
        
 
    @classmethod   
    def edition_products(cls):
        
        #Frame Geral Produtos
        cls.desc_frame = CTkFrame(
            master=cls.app_description, 
            fg_color="#E1E1E1",  
            width=450, 
            height=650, 
            corner_radius=0)
        cls.desc_frame.pack_propagate(0)
        cls.desc_frame.pack(fill="y", anchor="w", side="left")
        
        #Frame para elementos  #teste
        cls.desc_frame_uni = CTkFrame(
            master=cls.desc_frame, 
            fg_color="#E1E1E1",  
            width=300, 
            height=400, 
            corner_radius=0)
        cls.desc_frame_uni.pack_propagate(0)
        cls.desc_frame_uni.pack(anchor="n")
        
        #teste frame teste
        cls.text_description = "Insira os dados do Produto"
        
        cls.tit_desc = CTkLabel(
            master=cls.desc_frame_uni, 
            text= cls.text_description, 
            font= ("Verdana", 14, "bold"),
            text_color="#045A87")
        cls.tit_desc.pack(pady=(10), anchor="center")
        
        # CAMPO: NOME
        cls.name = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Nome:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.name.pack(fill="x", anchor="n", pady=(0), side= LEFT)
        cls.name.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.17, anchor="w") 
      
        # FRAME PARA BD DO NOME 
        cls.frame_cod_barra = CTkEntry(master=cls.desc_frame_uni,
                                 fg_color="white",  
                                 width=200, 
                                 height=30, 
                                 corner_radius=0)
        cls.frame_cod_barra.pack_propagate(0)
        cls.frame_cod_barra.pack(fill="y", anchor="n", pady=(0), padx= (60,0))
        
        
        # CAMPO: CODIGO DE BARRAS
        cls.frame_cod_barra_label = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Codigo:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.frame_cod_barra_label.pack(anchor="n", pady=(0), side= LEFT)
        cls.frame_cod_barra_label.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.30, anchor="w") 

        # FRAME PARA MARCA DO PRODUTO
        cls.frame_marca = CTkEntry(master=cls.desc_frame_uni,
                                   fg_color="white",  
                                   width=200, 
                                   height=30,
                                   corner_radius=0)
        cls.frame_marca.pack(fill="y", anchor="n", pady=(10), padx= (60,0))

        # Adicione esta linha para tornar o rótulo "Marca" um filho do quadro
        #cls.brand_label.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.37, anchor="w") 
        
        # BOX CATEGORIA
        cls.category_label = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Categoria:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.category_label.pack(anchor="n", pady=(0), side= LEFT)
        cls.category_label.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.41, anchor="w") 

        
        cls.box_categoria= CTkComboBox(master=cls.desc_frame_uni,
                                     values=["Vegetais", "Fruta", "Verdura", "Açougue", "Não perecíveis", "Peixaria", "Congelados", "Frios", "Bebidas", "Outros"],
                                     button_color="#008DD2",
                                     border_color="#008DD2",
                                     button_hover_color="#008DD2",
                                     dropdown_hover_color="#008DD2",
                                     dropdown_fg_color="#E1E1E1",
                                     dropdown_text_color="#000000",
                                     width=200,
                                     height=30, 
                                     )
        cls.box_categoria.pack(fill="y", anchor="n", pady=(0), padx= (60,0))
        #expand=True)
        
        # BOX DESCRIÇÃO
        cls.descr_label = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Descrição:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.descr_label.pack(anchor="n", pady=(0), side= LEFT)
        cls.descr_label.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.55, anchor="nw") 
        
        cls.frame_descr = CTkEntry(master=cls.desc_frame_uni,
                                   fg_color="white",  
                                   width=200, 
                                   height=60,
                                   corner_radius=0)
        cls.frame_descr.pack(fill="y", anchor="n", pady=(10), padx= (60,0))

        """
        cls.scrollable_frame = CTkScrollableFrame(cls.desc_frame_uni, fg_color="white", width=200,height=20)
        cls.scrollable_frame.pack(pady=0, side=LEFT)
        cls.text_descricao = "Bla, bla, bla, Bla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla,"
        cls.texto = CTkLabel(cls.scrollable_frame,text=cls.text_descricao, justify = CENTER ).pack()"""

        # CAMPO marca:
        cls.brand_label = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Marca:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.brand_label.pack(anchor="n", pady=(0), side= LEFT)
        cls.brand_label.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.74, anchor="w")
        
        cls.frame_brand = CTkEntry(master=cls.desc_frame_uni,
                                   fg_color="white",  
                                   width=200, 
                                   height=30,
                                   corner_radius=0)
        cls.frame_brand.pack(fill="y", anchor="n", pady=(0), padx= (60,0))
        
        # CAMPO VALOR:
        cls.vallue_label = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Valor:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.vallue_label.pack(anchor="n", pady=(0), side= LEFT)
        cls.vallue_label.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.80, anchor="w")
        
        cls.frame_vallue = CTkEntry(master=cls.desc_frame_uni,
                                   fg_color="white",  
                                   width=200, 
                                   height=30,
                                   corner_radius=0)
        cls.frame_vallue.pack(fill="y", anchor="n", pady=(0), padx= (60,0))
        
        # Button Maiores informacoes
        cls.button_prod = CTkButton(master=cls.desc_frame_uni, 
                                    fg_color="#E1E1E1",
                                    text="Guardar informação", 
                                    font=("Verdana", 12), 
                                    text_color="#000000",
                                    border_color= "008DD2")
        cls.button_prod.pack(pady=(0), anchor="n")
        
        
        #DESCRIÇÃO
        """cls.text_descricao = "Bla, bla, bla, Bla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla,"
        
        cls.scrollable_frame = CTkScrollableFrame(cls.desc_frame_uni, fg_color="red")
        cls.scrollable_frame.pack(pady=0)
        
        cls.texto = CTkLabel(cls.scrollable_frame,text=cls.text_descricao, justify = CENTER ).pack()"""
        # create scrollable textbox

        #INSERIR O PRODUTO 
        
        
        
        
        
if __name__ == '__main__':
    AppEditProduct()   