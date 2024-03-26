from pathlib import Path
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk

PATH = Path(__file__).parent.parent / "assets"

class InsertSupplier:
    root = ttk.Window(themename="cosmo")
    def __init__(self):
        super().__init__()
        
        self.window_supplier()
        self.frame_photo_supplier()
        self.entrys_supplier()
        
        # form entries
        self.name = ttk.StringVar(value="") 
        self.address = ttk.StringVar(value="")
        self.phone = ttk.DoubleVar(value=0.0)
        self.email = ttk.StringVar(value="")
        
        self.create_form_supplier("Nome:", self.name.get())
        self.create_form_supplier("Endereço:", self.address.get())
        self.create_form_supplier("Telefone:", self.phone.get())
        self.create_form_supplier("E-mail:", self.email.get())

        self.create_buttonbox()
        #self.root.configure(background='blue')
        self.root.mainloop()
        
    @ classmethod
    def window_supplier(cls):
        cls.root.title("Inserir Fornecedores")
        cls.root.geometry('1000x650')
        cls.root.minsize(width=756, height=545)
        
    @ classmethod
    def frame_photo_supplier(cls):
        # Frame para dividir a tela. 
        prod_frame_description = ttk.Frame(cls.root, width=300, height=1000)
        prod_frame_description.pack(fill=tk.Y, side=LEFT)
        
        style = ttk.Style()
        style.configure("Custom.TFrame", background=style.colors.primary, )
        

        prod_frame_description.config(style="Custom.TFrame", )
        
    
        img_supplier = Image.open(PATH / "page/supplier.png")
        cls.img_supplier = ImageTk.PhotoImage(img_supplier.resize((252, 252)))
        cls.button1 = Label(
            prod_frame_description, width=250, height=250, image=cls.img_supplier, text="", borderwidth= 0, highlightthickness=0, bd=0
        ).place(relx=.08, rely=.3)
        
        return prod_frame_description
    
    @classmethod
    def entrys_supplier(cls):
        register_prod = ttk.Frame(cls.root, padding=(20, 10))
        register_prod.pack(fill=BOTH, expand=YES)
        #Colocando cor na frame 
          
        
        # form header
        hdr_txt = "Digite os dados do fornecedor:" 
        hdr = ttk.Label(register_prod, text=hdr_txt, width=50, font=("Verdana", 18))
        style = ttk.Style()
        style.configure("Custom.TLabel", foreground=style.colors.primary, )
        hdr.config(style="Custom.TLabel",)

    
        hdr.pack(pady=20)
        
    
    @ classmethod    
    def create_form_supplier(cls, label, variable): 
        #Criar uma unica entrada no formulario
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = Entry(master=container, textvariable=variable, bg="white", relief="solid", borderwidth= 0.5)
        #ent.pack(padx=5, pady=5)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        
        return ent

    @ classmethod    
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
        sub_btn.pack(side=RIGHT, padx=20)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=cls.on_cancel,
            bootstyle='DANGER',
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)    
     
    """ TIPO DE ACESSO - FAZER COMBOBOX Admin = "Admin" | SubAdmin = "Sub_Admin" | User = "User"""
    @classmethod
    def combobox_type_user(cls):
        frame_combobox = ttk.Frame(cls.root)
        frame_combobox.pack(fill=X, expand=YES, pady=5)
        
        lbl_combobox = ttk.Label(frame_combobox, text="Tipo de Acesso", width=13)
        lbl_combobox.pack(side=LEFT, padx=5)
         
        type_acess = ttk.Combobox(frame_combobox, state="readonly", values=["Admin", "Sub_Admin", "User"])
        type_acess.current(0)
        type_acess.pack(side=LEFT, padx=20, fill=X, expand=YES)
        
        return type_acess

    @classmethod    
    def on_submit(cls):
        #IMPRIME CONTEUDO E RETORNA OS VALORES
        print("Nome:", cls.name.get())
        print("Endereço:", cls.address.get())
        print("Telefone:", cls.phone.get())
        print("E-mail:", cls.email.get())
        
        return cls.address.get(), cls.name.get(), cls.phone.get(), cls.email.get()
    
    
    @classmethod    
    def on_cancel(self):
        #Cancela e sai da app
        self.quit()
       
if __name__ == '__main__':
    inicio = InsertSupplier() 
    # Test code

    inicio.root.mainloop()        
