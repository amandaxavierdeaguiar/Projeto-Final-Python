from pathlib import Path
from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
<<<<<<<< HEAD:viewBootstrap/register_product_old._old.py
from tkinter import filedialog
========
from sqlmodel import Session
>>>>>>>> 9511b177a5246a2968ccd153ad9314767dd28039:viewBootstrap/register_product_old.py
from ttkbootstrap import Style

from controllers.BrandController import BrandController
from controllers.CategoryController import CategoryController
from models.db.db_conection import get_session

PATH = Path(__file__).parent / "assets"


class InsertProduct:
    root = ttk.Window(themename="cosmo")
    ctrl_brand: BrandController = BrandController()  # <-
    ctrl_category: CategoryController = CategoryController()  # <-
    session: Session = get_session()  # <-
    prod_frame: ttk.Frame
    name: StringVar
    name_ent: Entry
    bar_cod: ttk.IntVar
    description: ttk.StringVar
    price: ttk.DoubleVar
    category: ttk.StringVar
    brand: ttk.StringVar

    def __init__(self):
        super().__init__()

        self.window_product()
<<<<<<<< HEAD:viewBootstrap/register_product_old._old.py
        self.frame_photo_product()
        self.entrys_product()
        
========
        self.prod_frame = self.frame_photo_product()
        self.title_frame()
        # self.entrys_product()

>>>>>>>> 9511b177a5246a2968ccd153ad9314767dd28039:viewBootstrap/register_product_old.py
        # form entries
        self.name = StringVar(value="")
        self.bar_cod = ttk.IntVar(value=None)
        self.description = ttk.StringVar(value="")
        self.price = ttk.DoubleVar(value=None)
        self.category = ttk.StringVar(value="")
<<<<<<<< HEAD:viewBootstrap/register_product_old._old.py
        self.brand = ttk.StringVar(value="")      
        
        """self.create_form_entry("Nome", self.name.get)
        self.create_form_entry("Cod_Barra", self.bar_cod.get)
        self.create_form_entry("Descrição", self.description.get)
        self.create_form_entry("Preço", self.price.get)"""
        
        self.create_form_entry("Nome", self.name, "text")
        self.create_form_entry("Cod_Barra", self.bar_cod, "text")
        self.create_form_entry("Descrição", self.description, "text")
        self.create_form_entry("Preço", self.price, "double")
        
        self.create_combobox_category()
        self.create_combobox_brand()
        self.textbox_description()
        self.create_buttonbox()
========
        self.brand = ttk.StringVar(value="")

        self.name_ent = self.create_form_entry("Nome", self.name)
        self.create_form_entry("Cod_Barra", self.bar_cod)
        self.create_form_entry("Preço", self.price)
        self.create_combobox("Categoria:", self.ctrl_category.get_all(self.session))
        self.create_combobox("Marca:", self.ctrl_brand.get_all(self.session))
        self.textbox_description()
        self.create_buttonbox()

>>>>>>>> 9511b177a5246a2968ccd153ad9314767dd28039:viewBootstrap/register_product_old.py
        self.root.mainloop()

    @classmethod
    def window_product(cls):
        cls.root.title("Inserir Produtos")
        cls.root.geometry("1000x650")
        cls.root.minsize(width=756, height=545)

    @classmethod
    def frame_photo_product(cls):
        # Frame para dividir a tela.
        prod_frame = ttk.Frame(cls.root, width=300, height=1000)
<<<<<<<< HEAD:viewBootstrap/register_product_old._old.py
        prod_frame.pack(fill=Y, side=LEFT)
    
        style = ttk.Style()
        style.configure("Custom.TFrame", background=style.colors.primary)
        style.configure("Custom.Button", background=style.colors.info, )
        prod_frame.config(style="Custom.TFrame", )
        
        img_logo = Image.open(PATH / "logo-stock-b.png")
        cls.img_logo = ImageTk.PhotoImage(img_logo.resize((250, 250)))
        cls.button1 = Label(
            prod_frame, width=250, height=250, image=cls.img_logo, text="", pady=40
        ).place(relx=.07, rely=.1)
        
        button_insert_img = Button(
            prod_frame,
            text="ADICIONE A IMAGEM",
            cursor="hand2",
            command=cls.on_select_image, # Acrescentei
        )
        button_insert_img.place(relx=.2, rely=.6)
        
        
========
        prod_frame.pack(fill=tk.Y, side=LEFT)

        style = ttk.Style()
        style.configure("Custom.TFrame", background=style.colors.primary)
        style.configure(
            "Custom.Button",
            background=style.colors.info,
        )
        prod_frame.config(
            style="Custom.TFrame",
        )

        button_insert_img = ttk.Button(
            prod_frame,
            text="ADICIONE A IMAGEM",
            cursor="hand2",
        )
        button_insert_img.place(relx=0.3, rely=0.5)
        return prod_frame

>>>>>>>> 9511b177a5246a2968ccd153ad9314767dd28039:viewBootstrap/register_product_old.py
    @classmethod
    def title_frame(cls):
        register_prod = ttk.Frame(cls.root, padding=(20, 10))
        register_prod.pack(fill=BOTH, expand=YES)

        # form header
        hdr_txt = "Digite os dados do produto:"
        hdr = ttk.Label(register_prod, text=hdr_txt, width=50, font=("Verdana", 18))
        hdr.pack(pady=20)
<<<<<<<< HEAD:viewBootstrap/register_product_old._old.py
        
    
    """@ classmethod    
    def create_form_entry(cls, label, variable): 
        #Criar uma unica entrada no formulario
========

    @classmethod
    def create_form_entry(cls, label, variable):
        # Criar uma unica entrada no formulario
>>>>>>>> 9511b177a5246a2968ccd153ad9314767dd28039:viewBootstrap/register_product_old.py
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10, anchor="e")
        lbl.pack(side=LEFT, padx=5)

<<<<<<<< HEAD:viewBootstrap/register_product_old._old.py
        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)"""
        
    @classmethod
    def create_form_entry(cls, label, variable, entry_type):
        # Criar uma unica entrada no formulario
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        if entry_type == "image":
            ent = ttk.Button(master=container, text="Procurar imagem", command=cls.on_select_image)
            ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        else:
            ent = ttk.Entry(master=container, textvariable=variable)
            ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        # Create a label to display the form entry
        label_entry = ttk.Label(master=container, text=variable.get())
        label_entry.pack(side=LEFT, padx=5)
        
    @classmethod
    def on_select_image(cls):
        # Open a file dialog to select an image
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])

        # Display the selected image in the GUI
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label_image = ttk.Label(master=cls.frame_photo_product, image=photo)
        label_image.image = photo
        label_image.pack(fill=X, expand=YES)

        # Store the image path in the class variable
        cls.image_path = file_path
     
     
    @ classmethod
    def create_combobox_category(cls):
========
        ent = Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        return ent

    @classmethod
    def create_combobox(cls, label, variable):
>>>>>>>> 9511b177a5246a2968ccd153ad9314767dd28039:viewBootstrap/register_product_old.py
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=5)
        lbl = ttk.Label(master=container, text=label, width=10, anchor="e")
        lbl.pack(side=LEFT, padx=5)

        ent_combobox = ttk.Combobox(
            master=container,
            values=variable,
            state="readonly",
        )
        ent_combobox.pack(side=LEFT, padx=5, fill=X, expand=YES)
        # (expand=True, side=NONE, padx=5)

        return ent_combobox

    @classmethod
    def textbox_description(cls):
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=5)
        lbl = ttk.Label(master=container, text="Descrição:", width=10, anchor="e")
        lbl.pack(side=LEFT, padx=5)

        ent_description = ttk.ScrolledText(master=container, wrap=WORD, height=5)
        ent_description.pack(side=LEFT, padx=5, fill=X, expand=YES)

    @classmethod
    def create_buttonbox(cls):
        """Caixa Botoes App"""
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=cls.on_submit,
            bootstyle="SUCCESS",
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=cls.on_cancel,
            bootstyle="DANGER",
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    @classmethod
    def on_submit(cls):
        # IMPRIME CONTEUDO E RETORNA OS VALORES
        print("Nome:", cls.name_ent.get())
        print("Codigo Barras:", cls.bar_cod.get())
        print("Descrição:", cls.description.get())
        print("Preço:", cls.price.get())
        print("Categoria:", cls.category.get())
        print("Marca:", cls.brand.get())
        return (
            cls.bar_cod.get(),
            cls.name.get(),
            cls.description.get(),
            cls.price.get(),
            cls.brand.get(),
        )

    # cls.category.get()

    @classmethod
    def on_cancel(cls):
        # Cancela e sai da app
        cls.quit()


if __name__ == "__main__":
    inicio = InsertProduct()
    inicio.root.mainloop()
