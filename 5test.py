
import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk

root = Tk.Tk()
F = Figure(figsize=(13, 3), dpi=100)
re = F.add_subplot(1,1,1)
canvas = FigureCanvasTkAgg(F, master=root)
canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=0)
canvas._tkcanvas.pack(side=Tk.TOP, expand=0)

def Make_graphs():
    arr = np.random.rand(2048)
    re.cla()
    re.plot(arr, linestyle='-')
    #re.ylim(0,1)
    re.set_ylim([0,1])
    canvas.draw()
    root.after(1, Make_graphs)

Make_graphs()
root.mainloop()
