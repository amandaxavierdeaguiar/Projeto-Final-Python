from pathlib import Path
from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk

PATH = Path(__file__).parent / "assets"

class InsertUser:
    root = ttk.Window(themename="cosmo")
    def __init__(self):
        super().__init__()
        
        self.window_user()
        self.frame_photo_user()
        self.entrys_user()
        
        # form entries
        self.name = ttk.StringVar(value="") 
        self.login = ttk.StringVar(value="")
        self.password = ttk.DoubleVar(value=0.0)
        self.typeAcess = ttk.StringVar(value="")
        
        self.create_form_user("Nome:", self.name.get())
        self.create_form_user("Login:", self.login.get())
        self.create_form_user("Password:", self.password.get())
        self.create_form_user("Tipo de Acesso:", self.typeAcess.get())

        self.create_buttonbox()
        #self.root.configure(background='blue')
        self.root.mainloop()
        
    @ classmethod
    def window_user(cls):
        cls.root.title("Adicionar Usuário")
        cls.root.geometry('1000x650')
        cls.root.minsize(width=756, height=545)
        
    @ classmethod
    def frame_photo_user(cls):
        # Frame para dividir a tela. 
        prod_frame_description = ttk.Frame(cls.root, width=300, height=1000)
        prod_frame_description.pack(fill=tk.Y, side=LEFT)
        
        style = ttk.Style()
        style.configure("Custom.TFrame", background=style.colors.primary, )
        

        prod_frame_description.config(style="Custom.TFrame", )
        
    
        img_user = Image.open(PATH / "insert_user_bg2.png")
        cls.img_user = ImageTk.PhotoImage(img_user.resize((250, 250)))
        cls.button1 = Label(
            prod_frame_description, width=250, height=250, image=cls.img_user, text="", borderwidth= 0
        ).place(relx=.08, rely=.3)
        
        return prod_frame_description
    
    @classmethod
    def entrys_user(cls):
        register_prod = ttk.Frame(cls.root, padding=(20, 10))
        register_prod.pack(fill=BOTH, expand=YES)
        #Colocando cor na frame 
          
        
        # form header
        hdr_txt = "Digite os dados do produto:" 
        hdr = ttk.Label(register_prod, text=hdr_txt, width=50, font=("Verdana", 18))
        style = ttk.Style()
        style.configure("Custom.TLabel", foreground=style.colors.primary, )
        hdr.config(style="Custom.TLabel",)

    
        hdr.pack(pady=20)
        
    
    @ classmethod    
    def create_form_user(cls, label, variable): 
        #Criar uma unica entrada no formulario
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=13)
        lbl.pack(side=LEFT, padx=5)

        ent = Entry(master=container, textvariable=variable, bg="white", relief="solid", borderwidth= 0.5)
        #ent.pack(padx=5, pady=5)
        ent.pack(side=LEFT, padx=20, fill=X, expand=YES)
        
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
        #IMPRIME CONTEUDO E RETORNA OS VALORES
        print("Nome:", cls.name.get())
        print("Login:", cls.login.get())
        print("Password:", cls.password.get())
        print("Tipo de Acesso:", cls.typeAcess.get())
        
        return cls.name.get(), cls.login.get(), cls.password.get(), cls.typeAcess.get()
    
        

    
    @classmethod    
    def on_cancel(cls):
        #Cancela e sai da app
        cls.quit()
       
if __name__ == '__main__':
    inicio = InsertUser() 
    # Test code

    inicio.root.mainloop()        
