from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style

class InsertProduct:
    root = ttk.Window(themename="lumen")
    def __init__(self):
        super().__init__()
    
        self.window_product()
        self.frame_photo_product()
        self.register_product()
        self.root.mainloop()
        
    @ classmethod
    def window_product(cls):
        cls.root.title("Inserir Produtos")
        cls.root.geometry('1000x650')
        cls.root.minsize(width=756, height=545)
        
    @ classmethod
    def frame_photo_product(cls):
        # FRAME PARA DIVISAO DE TELA
        main_frame_prod = tk.Frame(cls.root, width=350, height=650, bg="black") 
        #main_frame_prod.pack(fill=BOTH, side="left")
        main_frame_prod.pack(fill="y", anchor="w", side="left")
        
        # FRAME PARA POR A FOTO
        cls.photo_bd_frame = tk.Frame(main_frame_prod, width= 350, height=350, bg="blue")
        cls.photo_bd_frame.pack_propagate(0)
        cls.photo_bd_frame.place(relwidth=1, relheight=1)
        
    @classmethod
    def register_product(cls):
           
        prod_img = Image.open('assets/add_products.png')
        new_img = prod_img.resize((100,100))
        img_prod = ImageTk.PhotoImage(new_img)
        cls.lbl_image = tk.Label(cls.photo_bd_frame, image=img_prod)
        cls.lbl_image.grid(row=0 , column=0, padx=10, pady=10)
        

        
if __name__ == '__main__':
    
        inicio = InsertProduct()
        inicio.root.mainloop()

