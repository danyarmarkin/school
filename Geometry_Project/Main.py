import tkinter as tk
from Coord import *
from random import random
from figures import *

root = tk.Tk()

root.geometry("1080x720")
root.title("Geometry")

grid_frame = Frame(root)
grid_frame.config(width=400, height=400)
grid = Grid(grid_frame)
grid.drawGrid()
grid.drawAxis()

for i in range(10):
    x = random() * 20 - 10
    y = random() * 20 - 10
    print(x, y)
    grid.addDot(Dot(x, y))

grid.clear()

grid_frame.grid(row=0, column=0)
root.mainloop()