from customtkinter  import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x300')

        self.frame= CTkFrame(self, fg_color='light blue', width=200, height=self.winfo_height())
        self.frame.pack_propagate(False)
        self.frame.configure(width=0)
        self.frame.place(x=0, y=0)
        self.is_show_menu = False
        self.frame_widht = 0

        self.label = CTkLabel(self.Frame, text='Ваше ім'я')
        self.label.pack(pady=30)