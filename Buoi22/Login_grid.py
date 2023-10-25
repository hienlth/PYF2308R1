from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('LOGIN FORM')
root.geometry("230x170")

Label(root, text="LOGIN FORM", fg="red", font="Arial 16").grid(row=0, column=0, columnspan=2)
# bg: màu nền (background), fg: màu chữ (foreground)

Label(root, text="Username:").grid(row=1, column=0, pady=5)
Entry(root).grid(row=1, column=1, pady=5)

Label(root, text="Email:").grid(row=2, column=0, pady=5)
Entry(root).grid(row=2, column=1, pady=5)

Label(root, text="Password:").grid(row=3, column=0, pady=5)
Entry(root).grid(row=3, column=1, pady=5)

def handle_login():
    messagebox.showinfo(title='HAHAHAH', message="AAAA")
    
btnLogin = ttk.Button(root, text="Login", command=handle_login)
btnLogin.grid(row=4, column=1, pady=5)

root.mainloop()