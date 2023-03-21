import tkinter as tk
from functools import partial

import Coord
from WorkSpace import *

root = tk.Tk()  # создаем окно

root.geometry("1080x720")
root.title("Годовой проект по геометрии за 10 класс")

work_space = WorkSpace(root)
work_space.grid(row=0, column=0)

grid_frame = Frame(root)
grid_frame.config(width=200, height=200)
grid = Coord.Grid(grid_frame)
grid.drawGrid()
grid.drawAxis()
grid_frame.place(x=400, y=50)


# функция помощи
def help():
    help_root = Tk()
    help_root.geometry("600x400")
    help_root.title("Помощь")
    h = Label(help_root, text=""" Помощь
    
    Ввод:
    1. Клавиатура -- ввести точки при помощи клавиатуры
    2. Мышь -- ввести точки при помощи мыши
    3. Файл -- ввести точки из выбранного файла
    4. Случайно -- ввести точки рандомайзером, указав их количество
    
    Вывод:
    1. Экран -- показать координаты точек на экране
    2. Файл -- записать координаты точек в файл (файл сохраниться в папку проекта)
    
    Редактирование:
    1. Удалить все точки -- удаление всех точек из памяти
    2. Редактировать -- редактировать точки
    
    Вычисление:
    1. Вычислить -- вычислить и продемонстрировать решение
    """)
    h.grid(row=0, column=0)


# функция условия
def about():
    help_root = Tk()
    help_root.geometry("600x400")
    help_root.title("Помощь")
    h = Label(help_root, text="""Условие:
    Дано множество точек на плоскости.
    Определить среди них подмножество точек наибольшего размера такое,
    что каждая точка этого множества является вершиной хотя
    бы двух равносторонних треугольников,
    вершины которого принадлежат этому подмножеству.
    Ответом будет множество всех таких равносторонних треугольников
        """)
    h.grid(row=0, column=0)


# создаем меню
mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu1 = Menu(mainmenu, tearoff=0)
filemenu1.add_command(label="Клавиатура", command=partial(work_space.addDotWithKeyboard, grid))
filemenu1.add_command(label="Мышь", command=partial(work_space.addDotsWithMouse, grid))
filemenu1.add_command(label="Файл", command=partial(work_space.importDotsFromFile, grid))
filemenu1.add_command(label="Случайно", command=partial(work_space.addDotWithRandom, grid))
filemenu2 = Menu(mainmenu, tearoff=0)
filemenu2.add_command(label="Файл", command=partial(work_space.writeDotsToFile, grid))
filemenu2.add_command(label="Экран", command=partial(work_space.showDots, grid))
filemenu3 = Menu(mainmenu, tearoff=0)
filemenu3.add_command(label="Удалить все точки", command=grid.clear)
filemenu3.add_command(label="Редактировать", command=partial(work_space.editDots, grid))
filemenu4 = Menu(mainmenu, tearoff=0)
filemenu4.add_command(label="Вычислить", command=grid.solutions)
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь", command=help)
helpmenu.add_command(label="О программе", command=about)
mainmenu.add_cascade(label="Ввод", menu=filemenu1)
mainmenu.add_cascade(label="Вывод", menu=filemenu2)
mainmenu.add_cascade(label="Редактирование", menu=filemenu3)
mainmenu.add_cascade(label="Вычисление", menu=filemenu4)
mainmenu.add_cascade(label="Справка", menu=helpmenu)
mainmenu.add_command(label="Выход", command=exit)

root.mainloop()
