import tkinter as tk
import Coord
from random import random
from figures import *
from WorkSpace import *

root = tk.Tk()

root.geometry("1080x720")
root.title("Geometry")

work_space = WorkSpace(root)
# work_space.addDot()
work_space.grid(row=0, column=0)

grid_frame = Frame(root)
grid_frame.config(width=200, height=200)
grid = Coord.Grid(grid_frame)
grid.drawGrid()
grid.drawAxis()
grid_frame.place(x=400, y=50)



mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu1 = Menu(mainmenu, tearoff=0)
filemenu1.add_command(label="Клавиатура", command=partial(work_space.addDotWithKeyboard, grid))
filemenu1.add_command(label="Мышь", command=partial(work_space.addDotsWithMouse, grid))
filemenu1.add_command(label="Файл", command=partial(work_space.importDotsFromFile, grid))
filemenu1.add_command(label="Random", command=partial(work_space.addDotWithRandom, grid))
filemenu2 = Menu(mainmenu, tearoff=0)
filemenu2.add_command(label="Файл", command=partial(work_space.writeDotsToFile, grid))
filemenu2.add_command(label="Экран", command=partial(work_space.showDots, grid))
filemenu3 = Menu(mainmenu, tearoff=0)
filemenu3.add_command(label="Очистить экран", command=grid.clear)
filemenu3.add_command(label="Редактировать", command=partial(work_space.editDots, grid))
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")
mainmenu.add_cascade(label="Ввод", menu=filemenu1)
mainmenu.add_cascade(label="Вывод", menu=filemenu2)
mainmenu.add_cascade(label="Редактирование", menu=filemenu3)
mainmenu.add_cascade(label="Вычисление")
mainmenu.add_cascade(label="Демонстрация")
mainmenu.add_cascade(label="Справка", menu=helpmenu)
mainmenu.add_command(label="Выход", command=exit)

root.mainloop()