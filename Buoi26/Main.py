from tkinter import *
from tkinter import ttk, messagebox
import random

root = Tk()
root.title("GAME")
root.geometry("400x400")

colors = [
	"red", "blue", "yellow", "magenta" 
]

def generate_color(mylabel):	
    global selected_color
    selected_color = random.randint(0, len(colors) - 1)
    mylabel["bg"] = colors[selected_color]

def MH_COLORS():
    color_gui = Toplevel(root)
    color_gui.geometry("200x100")
    
    label_mau = Label(color_gui, text="________________", bg="yellow")
    generate_color(label_mau)
    label_mau.pack()
    
    color_gui.mainloop()
    
    
Button(root, text="COLORs", command=MH_COLORS).pack()


root.mainloop()
