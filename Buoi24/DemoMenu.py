from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from MyMenu import create_menu_file

root = Tk()
root.geometry("400x300")

# ================Màn hình con=================
def hien_man_hinh_con():
    mh_con = Toplevel(root)
    mh_con.geometry("300x300")
    mh_con.title("MÀN HÌNH CON")
    
    main_menu = Menu(mh_con)
    mh_con.config(menu=main_menu)
    main_menu.add_cascade(label="Tool", menu=create_menu_file(main_menu, hien_man_hinh_con))

    ttk.Label(mh_con, text="ĐÂY LÀ MÀN HÌNH CON").pack(fill=X, padx=5, pady=5)
    
    mh_con.mainloop()
# ================End Màn hình con==============

# Menu chính (main menu)
menu_bar = Menu(root)
# nhúng menu vào màn hình chính
root.config(menu=menu_bar)


menu_bar.add_cascade(label="File", menu=create_menu_file(menu_bar, hien_man_hinh_con))


# Nhóm menu Help
mnu_help = Menu(menu_bar, tearoff=0)
mnu_help.add_command(label="About Jupyter", command=lambda: showinfo(title='ABOUT', message="MY APP"))
menu_bar.add_cascade(label="Help", menu=mnu_help)


root.mainloop()