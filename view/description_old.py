from customtkinter import *
import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel
from PIL import Image
import tkinter as tk
import customtkinter

"""" VOU A COM A JANELA DE EDIÇÃO, ASSIM QUE CLICA NO PRODUTO, JA MUDA OS DADOS(AINDA EM EXECUCAO)"""

class AppDescription:
    #ctrl_product: ProductController = ProductController()
    # ctrl: ProductController = ProductController()
    app_description: CTk = CTk()
    # session: Session = get_session()

    def __init__(self):
        super().__init__()

        self.windown()
        #self.description_frame()
        
        self.description_products()
        self.app_description.mainloop()

    @classmethod
    def windown(cls):
        cls.app_description.geometry("756x345")  # 756x545
        cls.app_description.title("Informações")  # Titulo página.
        cls.app_description.resizable(0, 0)

        set_appearance_mode("light")
        
    @classmethod    
    def img_products(cls):
        cls.prod_frame = CTkFrame(master=cls.app_description, fg_color="white",  width=350, height=650, corner_radius=0)
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
        
        cls.prod_img = Image.open("view/assets/alho_frances.png")
        cls.prod_img = CTkImage(light_image=cls.prod_img, 
                                size=(250, 250))
        cls.prod_img_label = CTkLabel(
            master=cls.photo_bd_frame, 
            text="", 
            image=cls.prod_img)
        cls.prod_img_label.pack(pady=(50, 0), anchor="center")
 
    @classmethod   
    def description_products(cls):
        
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
        cls.text_description = "Alho Francês"
        
        cls.tit_desc = CTkLabel(
            master=cls.desc_frame_uni, 
            text= cls.text_description, 
            font= ("Verdana", 20, "bold"),
            text_color="#045A87")
        cls.tit_desc.pack(pady=(20), anchor="center")
        
        # CAMPO: CODIGO DE BARRAS
        cls.cod_barras_label = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Codigo de Barras:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.cod_barras_label.pack(fill="x", anchor="n", pady=(0), side= LEFT)
        
        
        # FRAME PARA BD DO CODIGO DE BARRAS 
        cls.frame_cod = CTkFrame(master=cls.desc_frame_uni,
                                 fg_color="white",  
                                 width=200, 
                                 height=30, 
                                 corner_radius=0)
        cls.frame_cod.pack_propagate(0)
        cls.frame_cod.pack(fill="y", anchor="n", pady=(0))
         
        # CAMPO: MARCA
        cls.brand_label = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Marca:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.brand_label.pack(anchor="n", pady=(0), side= LEFT)

        # FRAME PARA MARCA DO PRODUTO
        cls.frame_marca = CTkFrame(master=cls.desc_frame_uni,
                                   fg_color="white",  
                                   width=200, 
                                   height=30,
                                   corner_radius=0)
        cls.frame_marca.pack(fill="y", anchor="n", pady=(10))

        # Adicione esta linha para tornar o rótulo "Marca" um filho do quadro
        cls.brand_label.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.37, anchor="w") 
        
        # BOX CATEGORIA
        cls.category_label = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Categoria:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.category_label.pack(anchor="n", pady=(0), side= LEFT)
        cls.category_label.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.48, anchor="w") 

        
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
        cls.box_categoria.pack(fill="y", anchor="n", pady=(0))
        #expand=True)
        
        # BOX DESCRIÇÃO
        cls.descr_label = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Descrição:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.descr_label.pack(anchor="n", pady=(0), side= LEFT)
        cls.descr_label.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.60, anchor="nw") 
        
        cls.frame_descr = CTkFrame(master=cls.desc_frame_uni,
                                   fg_color="white",  
                                   width=200, 
                                   height=60,
                                   corner_radius=0)
        cls.frame_descr.pack(fill="y", anchor="n", pady=(10))

        """
        cls.scrollable_frame = CTkScrollableFrame(cls.desc_frame_uni, fg_color="white", width=200,height=20)
        cls.scrollable_frame.pack(pady=0, side=LEFT)
        cls.text_descricao = "Bla, bla, bla, Bla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla, bla, blaBla,"
        cls.texto = CTkLabel(cls.scrollable_frame,text=cls.text_descricao, justify = CENTER ).pack()"""

        # CAMPO VALOR:
        cls.descr_label = CTkLabel(
            master=cls.desc_frame_uni, 
            text =  "Valor:", 
            text_color= "black", 
            font=("Verdana", 14))
        cls.descr_label.pack(anchor="n", pady=(0), side= LEFT)
        cls.descr_label.place(in_=cls.desc_frame_uni, relx=0.0, rely=0.80, anchor="w")
        
        cls.frame_preco = CTkFrame(master=cls.desc_frame_uni,
                                   fg_color="white",  
                                   width=200, 
                                   height=30,
                                   corner_radius=0)
        cls.frame_preco.pack(fill="y", anchor="n", pady=(0))
        
        # Button Maiores informacoes
        cls.button_prod = CTkButton(master=cls.desc_frame_uni, 
                                    fg_color="#E1E1E1",
                                    text="Editar produto", 
                                    font=("Verdana", 12), 
                                    text_color="#000000",
                                    border_color= "008DD2")
        cls.button_prod.pack(pady=(0), anchor="w", side= LEFT)
          
        
if __name__ == '__main__':
    AppDescription()   
    
    
    
