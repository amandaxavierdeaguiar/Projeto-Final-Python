import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style

class InsertProduct:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inserir Produto")
        self.root.geometry("1000x650")
        self.root.minsize(width=756, height=545)
        
        self.name = tk.StringVar()
        self.bar_cod = tk.StringVar()
        self.description = tk.StringVar()
        self.price = tk.DoubleVar()
        self.category = tk.StringVar()
        self.brand = tk.StringVar()
        self.image_path = tk.StringVar()
        
        self.frame_photo_product()
        self.entrys_product()
        self.create_buttonbox()
        
    @classmethod
    def frame_photo_product(cls):
        # Frame para dividir a tela.
        prod_frame = ttk.Frame(cls, width=300, height=1000)
        prod_frame.pack(fill=tk.Y, side=LEFT)
        
        style = ttk.Style()
        style.configure("Custom.TFrame", background=style.colors.primary)
        style.configure("Custom.Button", background=style.colors.info, )
        prod_frame.config(style="Custom.TFrame", )
        
        # Adicione a Foto
        cls.image_path.set("Nenhuma imagem selecionada")
        image_label = ttk.Label(prod_frame, textvariable=cls.image_path, width=20)
        image_label.place(relx=.3, rely=.5)
        
        def select_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.gif")])
            cls.image_path.set(file_path)
        
        button_insert_img = ttk.Button(
            prod_frame,
            text="Adicione a Foto",
            cursor="hand2",
            command=select_image
        )
        button_insert_img.place(relx=.3, rely=.5)
        
    @classmethod
    def entrys_product(cls):
        register_prod = ttk.Frame(cls.root, padding=(20, 10))
        register_prod.pack(fill=BOTH, expand=YES)
        
        # form header
        hdr_txt = "Digite os dados do produto:"
        hdr = ttk.Label(register_prod, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)
        
        cls.create_form_entry("Nome:", cls.name)
        cls.create_form_entry("Código de Barras:", cls.bar_cod)
        cls.create_form_entry("Descrição:", cls.description)
        cls.create_form_entry("Preço:", cls.price)
        cls.create_form_entry("Categoria:", cls.category)
        cls.create_form_entry("Marca:", cls.brand)
        
    @classmethod
    def create_form_entry(cls, label, variable):
        # Criar uma única entrada no formulário
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=5)

        ttk.Label(master=container, text=label, width=10).pack(side=LEFT, padx=5)
        ttk.Entry(master=container, textvariable=variable).pack(side=LEFT, padx=5, fill=X, expand=YES)

    @classmethod
    def create_buttonbox(cls):
        """Caixa Botoes App"""
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=cls.on_submit,
            bootstyle='SUCCESS',
            width=6,
        )
        sub_btn.pack(side='RIGHT', padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=cls.on_cancel,
            bootstyle='DANGER',
            width=6,
        )
        cnl_btn.pack(side='RIGHT', padx=5)
    
    @classmethod
    def on_submit(cls):
        # IMPRIME CONTEUDO E RETORNA OS VALORES
        print("Nome:", cls.name.get())
        print("Código de Barras:", cls.bar_cod.get())
        print("Descrição:", cls.description.get())
        print("Preço:", cls.price.get())
        print("Categoria:", cls.category.get())
        print("Marca:", cls.brand.get())
        return cls.bar_cod.get(), cls.name.get(), cls.description.get(), cls.price.get(), cls.category.get(), cls.brand.get()

    @classmethod
    def on_cancel(self):
        # Cancela e sai da app
        self.root.destroy()
        
if __name__ == '__main__':
    inicio = InsertProduct()
    inicio.root.mainloop()