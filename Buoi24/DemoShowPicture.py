import os
# print(os.getcwd()) # Lấy đường dẫn chính xác tới vị trí đang gọi file chạy
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

root = Tk()
root.geometry("400x300")


photo = PhotoImage(file="cs.png")
Label(root, image=photo).pack()

root.mainloop()