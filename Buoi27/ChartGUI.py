from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
  

root = Tk()
root.title('Plotting in Tkinter') 
root.geometry("500x500")

def plot():
    #====================Draw figure=================    
    fig = Figure(figsize = (5, 5), dpi = 100) 
  
    y = [i**2 for i in range(101)] 
  
    plot1 = fig.add_subplot(111) 
  
    plot1.plot(y) 
    #====================End Draw figure=================
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, master = root)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, root) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack()
  
# button that would displays the plot 
plot_button = Button(master = root, 
                     height = 2, 
                     width = 10, 
                    text = "Plot",
                    command=plot)

plot_button.pack() 
  
root.mainloop()