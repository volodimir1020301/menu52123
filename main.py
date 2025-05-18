from customtkinter import *
from random import *

win = CTk()
win.geometry('400x300')
win.title('соціальне опитування')
lbl = CTkLabel(win, text="Чи подобається тобі в логіці")
lbl.pack(pady=20)
def btn_no_func():
    new_x = randint(0, win.winfo_width() - btn_no.winfo_width())
    btn_no.place(x=new_x)
    new_y = randint(0, win.winfo_height() - btn_no.winfo_height())
    btn_no.place(y=new_y)
def hewwindow():
    win1 = CTk()
    win1.geometry('200x200')
    win1.title('приємно чути')
    lbl_win = CTkLabel(win1, text="приємно чути")
    lbl_win.pack(pady=20)


    win1.mainloop()

btn_no = CTkButton(win, text="ні", command=btn_no_func)
btn_no.place(x=70, y=100)

btn_yes = CTkButton(win, text="так", command=hewwindow)
btn_yes.place(x=220, y=100)


win.mainloop()