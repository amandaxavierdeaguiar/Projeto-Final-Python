from pathlib import Path
from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import filedialog

from requests import Session
from ttkbootstrap import Style

from controllers.BrandController import BrandController
from controllers.CategoryController import CategoryController
from controllers.ProductController import ProductController
from models.Product import Product
from models.db.db_conection import get_session

PATH = Path(__file__).parent / "assets"


class InsertProduct(ttk.Frame):
    root = ttk.Window(themename="cosmo")
    ctrl_brand: BrandController = BrandController()  # <-
    ctrl_category: CategoryController = CategoryController()  # <-
    ctrl_product: ProductController = ProductController()  # <-
    session: Session = get_session()  # <-
    file_name: str = ""
    prod_frame: ttk.Frame
    # nome
    name: StringVar = ttk.StringVar(value="")
    # bar code
    bar_cod: ttk.IntVar = ttk.IntVar(value=None)
    # description
    description: ttk.StringVar = ttk.StringVar(value="")
    # price
    price: ttk.DoubleVar = ttk.DoubleVar(value=None)
    # category
    category: ttk.StringVar = ttk.StringVar(value="")
    # Brand
    brand: ttk.StringVar = ttk.StringVar(value="")

    def __init__(self):
        super().__init__()

        self.window_product()
        self.prod_frame = self.frame_photo_product()
        self.title_frame()

        self.bar_cod_ent = self.create_form_entry("Cod_Barra", self.bar_cod, "text")
        self.name_ent = self.create_form_entry("Nome", self.name, "text")
        self.price_ent = self.create_form_entry("Preço", self.price, "double")
        self.category_ent = self.create_combobox("Categoria:", self.ctrl_category.get_all(self.session))
        self.brand_ent = self.create_combobox("Marca:", self.ctrl_brand.get_all(self.session))
        self.description_ent = self.textbox_description()
        self.create_buttonbox()
        self.root.mainloop()

    @classmethod
    def window_product(cls):
        cls.root.title("Inserir Produtos")
        cls.root.geometry('1000x650')
        cls.root.minsize(width=756, height=545)

    @classmethod
    def frame_photo_product(cls):
        # Frame para dividir a tela. 
        prod_frame = ttk.Frame(cls.root, width=300, height=1000)
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
                command=cls.on_select_image,  # Acrescentei
        )
        button_insert_img.place(relx=.2, rely=.6)
        return prod_frame

    @classmethod
    def title_frame(cls):
        register_prod = ttk.Frame(cls.root, padding=(20, 10))
        register_prod.pack(fill=BOTH, expand=YES)

        # form header
        hdr_txt = "Digite os dados do produto:"
        hdr = ttk.Label(register_prod, text=hdr_txt, width=50, font=("Verdana", 18))
        hdr.pack(pady=20)

    @classmethod
    def create_form_entry(cls, label, variable, entry_type):
        # Criar uma unica entrada no formulario
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10, anchor="e")
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
        return ent

    @classmethod
    def on_select_image(cls):
        # Open a file dialog to select an image
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
        file_path_strip = file_path.split('/')
        cls.file_name = file_path_strip[-1]
        # Display the selected image in the GUI
        image = Image.open(file_path)
        image.save(f"{PATH}/{cls.file_name}")
        photo = ImageTk.PhotoImage(image)
        label_image = ttk.Label(master=cls.prod_frame, image=photo)
        label_image.image = photo
        label_image.pack(fill=X, expand=YES)

        # Store the image path in the class variable
        cls.image_path = file_path

    @classmethod
    def create_combobox(cls, label, variable):
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
        lbl = ttk.Label(master=container, text="Descrição:", width=10)
        lbl.pack(side=LEFT, padx=5)

        ent_description = ttk.ScrolledText(master=container, wrap=WORD, height=5)
        ent_description.pack(side=LEFT, padx=5, fill=X, expand=YES)
        return ent_description

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
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
                master=container,
                text="Cancel",
                command=cls.on_cancel,
                bootstyle='DANGER',
                width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    @classmethod
    def on_submit(cls):
        # IMPRIME CONTEUDO E RETORNA OS VALORES
        category = cls.ctrl_category.get_by_name(cls.category.get(), cls.session)
        brand = cls.ctrl_brand.get_by_name(cls.brand.get(), cls.session)
        produto = Product()
        new_producto = produto.create(cls.bar_cod.get(), cls.name.get(), cls.file_name, cls.description.get(), cls.price.get(), brand.id, category.id)
        cls.ctrl_product.add(new_producto, cls.session)
    # cls.category.get()

    @classmethod
    def on_cancel(self):
        # Cancela e sai da app
        self.quit()


if __name__ == '__main__':
    inicio = InsertProduct()
    inicio.root.mainloop()
