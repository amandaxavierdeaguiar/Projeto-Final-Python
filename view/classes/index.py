from customtkinter import *
from menu import Menu
from stocks import StockList

""" Tenho que arrumar """
class Index:
    def __init__(self):
        super().__init__()

        self.app = CTk()
        self.app.geometry("856x645")
        self.app.title("Stock")
        self.app.resizable(0,0)

        set_appearance_mode("light")
        
        self.sidebar_frame = CTkFrame(master=self.app, fg_color="#008DD2",  width=176, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")
        
        self.button_menu = self.botoes_menu()
        self.button_inventory= self.inventory()
        
        self.app.mainloop()

    
    def botoes_menu(self):
        Menu()
            
    def inventory(self):
        StockList()
        
if  __name__ == "__main__":
    index = Index()
    