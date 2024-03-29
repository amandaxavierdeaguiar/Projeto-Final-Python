import tkinter
from pathlib import Path
from tkinter import *
from tkinter import filedialog

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from sqlmodel import Session

from controllers.BrandController import BrandController
from controllers.CategoryController import CategoryController
from controllers.ProductController import ProductController
from models.Product import Product
from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session
from views.Base.BaseWindow import BaseWindow

PATH = Path(__file__).parent.parent / "assets"


class ProductView(ttk.Frame):
    root = None
    ctrl_brand: BrandController = BrandController()  # <-
    ctrl_category: CategoryController = CategoryController()  # <-
    ctrl_product: ProductController = ProductController()  # <-
    session: Session = get_session()  # <-
    user: UserAuthentication
    file_name: ttk.StringVar
    type_request: str = ""
    main_frame: ttk.Frame
    main_note: ttk.Notebook
    # nome
    name: StringVar
    name_ent: Entry
    # Imagem Produto
    img_product: ImageTk.PhotoImage
    img_product_lbl: Label
    # bar code
    bar_cod: ttk.IntVar
    bar_cod_ent: Entry
    # description
    description: ttk.StringVar
    description_ent: ttk.ScrolledText
    # price
    price: ttk.DoubleVar
    price_ent: Entry
    # category
    category: ttk.IntVar
    category_ent: ttk.Combobox
    # Brand
    brand: ttk.IntVar
    brand_ent: ttk.Combobox

    def __init__(self, master_, note: ttk.Notebook, user_, type_="add", product_select=None):
        super().__init__(master_, padding=(10, 5))
        self.root = master_
        self.user = user_
        self.main_note = note
        (self.name, self.name_ent,
         self.bar_cod, self.bar_cod_ent,
         self.price_ent, self.price,
         self.description, self.description_ent,
         self.category_ent, self.category,
         self.brand, self.brand_ent, self.file_name) = self.create_vars(note, user_, type_, product_select)

    @classmethod
    def create_vars(cls, note: ttk.Notebook, user_, type_="add", product_select=None):
        photo_temp = (
            None
            if product_select is None or product_select["Foto"] == ""
            else product_select["Foto"]
        )
        cls.file_name = ttk.StringVar(value=photo_temp)
        name_temp = "" if product_select is None else product_select["Produto"]
        cls.name: StringVar = ttk.StringVar(value=name_temp)
        cls.name_ent = Entry()
        bar_cod_temp = "" if product_select is None else product_select["Bar Code"]
        cls.bar_cod: IntVar = ttk.IntVar(value=bar_cod_temp)
        cls.bar_cod_ent = Entry()
        description_temp = "" if product_select is None else product_select["Descrição"]
        cls.description: ttk.StringVar = ttk.StringVar(value=description_temp)
        cls.description_ent = ttk.ScrolledText()
        price_temp = None if product_select is None else float(product_select["Preço"])
        cls.price: ttk.DoubleVar = ttk.DoubleVar(value=price_temp)
        cls.price_ent = Entry()
        category_temp = (
            None if product_select is None else int(product_select["Categoria_id"])
        )
        cls.category: ttk.IntVar = ttk.IntVar(value=category_temp)
        cls.category_ent = ttk.Combobox()
        brand_temp = None if product_select is None else int(product_select["Marca_id"])
        cls.brand: ttk.IntVar = ttk.IntVar(value=brand_temp)
        cls.brand_ent = ttk.Combobox()
        return (cls.name, cls.name_ent,
                cls.bar_cod, cls.bar_cod_ent,
                cls.price_ent, cls.price,
                cls.description, cls.description_ent,
                cls.category_ent, cls.category,
                cls.brand, cls.brand_ent, cls.file_name)

    @classmethod
    def create_entries(cls, master, note: ttk.Notebook, user_, type_="add", product_select=None):
        cls.main_note = note
        cls.user = user_
        cls.create_vars(note, user_, type_, product_select)
        # self.main_frame = self.get_frame(self.main_note, type_, photo_temp, product_select)
        # nome
        cls.bar_cod_ent = cls.create_form_entry(master, "Bar Code", cls.bar_cod, "bar_code")
        # nome
        cls.name_ent = cls.create_form_entry(master, "Nome", cls.name, "text")
        # price
        cls.price_ent = cls.create_form_entry(master, "Preço", cls.price, "double")
        # category
        cls.category_ent = (
            cls.create_combobox(master,
                                 "Categoria:", cls.ctrl_category.get_all(cls.session), cls.category
                                ))
        cls.category_ent.current(cls.category.get())
        # Brand
        cls.brand_ent = (
            cls.create_combobox(master,
                                 "Marca:", cls.ctrl_brand.get_all(cls.session), cls.brand
                                ))
        cls.brand_ent.current(cls.brand.get())
        # description
        cls.description_ent = cls.textbox_description(master)
        # Buttons
        cls.create_buttonbox(master, type_)

    @classmethod
    def get_frame(cls, note, user_, type_, image_path=None, product_select=None):
        container = ttk.Frame(note, padding=60)
        container.pack(fill=BOTH, side=LEFT)
        # Frame para dividir a tela.
        img_frame = ttk.Frame(
            container, width=200, height=1000
        )

        img_frame.pack(fill=Y, side=RIGHT)
        if image_path is None:
            button_insert_img = Button(
                img_frame,
                text="ADICIONE A IMAGEM",
                cursor="hand2",
                command=cls.on_select_image,  # Acrescentei
            )
            button_insert_img.place(relx=0.2, rely=0.6)
        else:
            img_path_temp = Image.open(f"{PATH}\\products\\{image_path}")
            cls.img_product = ImageTk.PhotoImage(img_path_temp.resize((200, 200)))
            cls.img_product_lbl = ttk.Label(
                img_frame,
                width=200,
                image=cls.img_product,
                text="",
                padding=40,
            )
            cls.img_product_lbl.place(relx=0.07, rely=0.1)
        prod_frame = ttk.Frame(container, padding=60)
        prod_frame.pack(fill=BOTH, side=LEFT)
        cls.create_entries(container, note, user_, type_, product_select)
        return container

    @classmethod
    def create_form_entry(cls, note, label, variable, entry_type):
        # Criar uma unica entrada no formulario
        container = ttk.Frame(note)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10, anchor="e")
        lbl.pack(side=LEFT, padx=5)
        if entry_type == "image":
            ent = Button(
                master=container, text="Procurar imagem", command=cls.on_select_image
            )
            ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        elif entry_type == "bar_code":
            ent = ttk.Entry(master=container, textvariable=variable)
            ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        else:
            ent = ttk.Entry(master=container, textvariable=variable)
            ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        # Create a label to display the form entry
        label_entry = ttk.Label(master=container, text=variable)
        label_entry.pack(side=LEFT, padx=5)
        return ent

    @classmethod
    def on_select_image(cls):
        # Open a file dialog to select an image
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.png")]
        )
        file_path_strip = file_path.split("/")
        cls.file_name.set(value=file_path_strip[-1])
        # Display the selected image in the GUI
        image = Image.open(file_path)
        image.save(f"{PATH}/products/{cls.file_name.get()}")

    @classmethod
    def create_combobox(cls, note, label, values_, variable):
        container = ttk.Frame(note)
        container.pack(fill=X, expand=YES, pady=5)
        lbl = ttk.Label(master=container, text=label, width=10, anchor="e")
        lbl.pack(side=LEFT, padx=5)

        ent_combobox = ttk.Combobox(
            master=container,
            values=values_,
            textvariable=variable,
            state="readonly",
        )
        ent_combobox.pack(side=LEFT, padx=5, fill=X, expand=YES)
        return ent_combobox

    @classmethod
    def textbox_description(cls, note):
        container = ttk.Frame(note)
        container.pack(fill=X, expand=YES, pady=5)
        lbl = ttk.Label(master=container, text="Descrição:", width=10, anchor="e")
        lbl.pack(side=LEFT, padx=5)

        ent_description = ttk.ScrolledText(master=container, wrap=WORD, height=5)
        ent_description.pack(side=LEFT, padx=5, fill=X, expand=YES)
        return ent_description

    @classmethod
    def create_buttonbox(cls, note, type_):
        """Caixa Botoes App"""
        container = ttk.Frame(note)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        if type_ == 'add':
            sub_btn = ttk.Button(
                master=container,
                text="Submit",
                command=cls.on_submit_add,
                bootstyle="SUCCESS",
                width=6,
            )
            sub_btn.pack(side=RIGHT, padx=5)
            sub_btn.focus_set()
        elif type_ == 'update':
            sub_btn = ttk.Button(
                master=container,
                text="Submit",
                command=cls.on_submit_update,
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
    def create_new_product(cls):
        # IMPRIME CONTEUDO E RETORNA OS VALORES
        category = cls.ctrl_category.get_by_name(cls.category_ent.get(), cls.session)
        brand = cls.ctrl_brand.get_by_name(cls.brand_ent.get(), cls.session)
        produto = (Product(
            bar_cod=str(cls.bar_cod.get()),
            name=cls.name.get(),
            photo=cls.file_name.get(),
            description=cls.description_ent.get('1.0', tkinter.END).replace("\n", ""),
            price=cls.price.get(),
            brand_id=brand.id,
            category_id=category.id))
        return produto

    @classmethod
    def on_submit_add(cls):
        produto = cls.create_new_product()
        cls.ctrl_product.add(produto, cls.session)
        cls.main_note.forget(1)

    @classmethod
    def on_submit_update(cls):
        produto = cls.create_new_product()
        cls.ctrl_product.update(produto, cls.session)
        cls.main_note.forget(1)

    @classmethod
    def on_cancel(cls):
        # Cancela e sai da app
        cls.main_note.forget(1)
