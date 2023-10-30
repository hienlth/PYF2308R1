from tkinter import *

# Menu nhóm File
def create_menu_file(menu_main, show_child_gui):
    menu_file = Menu(menu_main, tearoff=False)
    menu_file.add_command(label="Mở MH Con", command=show_child_gui)
    menu_file.add_command(label="New")
    menu_file.add_command(label="Open")
    menu_file.add_command(label="Save")
    menu_file.add_command(label="Close")
    menu_file.add_separator()
    menu_file.add_command(label="Exit")
    
    return menu_file