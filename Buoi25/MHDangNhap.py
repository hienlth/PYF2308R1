from tkinter import *
from tkinter import ttk

def man_hinh_dang_nhap(main_ui):
    login_ui = Toplevel(main_ui)
    
    # Minimize taskbar
    main_ui.iconify()    
    
    login_ui.geometry("300x160")
    login_ui.title("LOGIN")
       
    Label(login_ui, text="LOGIN FORM", fg="red", font="Arial 16").place(x=90, y = 10)

    Label(login_ui, text="Username:").place(x=30, y=50)
    Entry(login_ui).place(x=100, y=50)

    Label(login_ui, text="Password:").place(x=30, y=80)
    Entry(login_ui).place(x=100, y=80)

    # Button(login_ui, text="Login", command=lambda: main_ui.withdraw()).place(x=110, y=110)
    Button(login_ui, text="Login").place(x=110, y=110)
    
    login_ui.mainloop()