from tkinter import *

root = Tk()
root.title('LOGIN FORM')
root.geometry("300x200")

Label(root, text="LOGIN FORM", fg="red", font="Arial 16").place(x=90, y = 10)
# bg: màu nền (background), fg: màu chữ (foreground)

Label(root, text="Username:").place(x=30, y=50)
Entry(root).place(x=100, y=50)

Label(root, text="Email:").place(x=30, y=90)
Entry(root).place(x=100, y=90)

Label(root, text="Password:").place(x=30, y=130)
Entry(root).place(x=100, y=130)

Button(root, text="Login").place(x=110, y=160)

root.mainloop()