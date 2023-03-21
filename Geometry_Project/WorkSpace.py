from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter.filedialog import askopenfilename

from figures import *
from random import random


class WorkSpace(Frame):

    # функция очистки
    def clear(self, grid):
        grid.canvas.unbind('<Button-1>')
        grid.canvas.unbind('<Motion>')
        grid.selected_dot = None
        grid.drawDots()
        for child in self.winfo_children():
            child.destroy()
        self.config(width=400, height=720)

    def __init__(self, root):
        super().__init__(root)
        self.activeDot = None
        self.config(width=400, height=720)

    # функция добавления точек мышью
    def addDotsWithMouse(self, grid):
        self.clear(grid)

        color = Entry(self)
        color.insert(END, "red")

        def onClick(event):
            x = round((event.x - grid.width * grid.size / 2) / grid.size, 1)
            y = round((grid.height * grid.size / 2 - event.y) / grid.size, 1)
            grid.addDot(Dot(x, y, color.get()))

        def unbind():
            grid.canvas.unbind('<Button-1>')

        grid.canvas.bind('<Button-1>', onClick)
        button = Button(self, text="Завершить расстановку точек", command=unbind)
        button.grid(row=0, column=0)
        color.grid(row=1, column=0)

    # функция добавления точек клавиатурой
    def addDotWithKeyboard(self, grid):
        self.clear(grid)
        helpLabel = Label(self, text="Введите координаты с клавиатуры X и Y")
        inputX = Entry(self)
        inputY = Entry(self)

        def dot():
            try:
                grid.addDot(Dot(float(inputX.get().replace(",", ".")), float(inputY.get().replace(",", ".")), "red"))
            except Exception:
                messagebox.showerror("Error", "Введите координаты точки правильно")

        enter = Button(self, text="Add dot", command=dot)
        helpLabel.grid(row=0, column=0)
        inputX.grid(row=1, column=0)
        inputY.grid(row=2, column=0)
        enter.grid(row=3, column=0)

    # функция добавления точек рандомом
    def addDotWithRandom(self, grid):
        self.clear(grid)
        helpLabel = Label(self, text="Введите количество точек (рекомедуется 50 - 150)")
        entry = Entry(self)

        def dot():
            n = int(entry.get())
            dots = []
            for _ in range(n):
                x = round(random() * grid.width - grid.width / 2, 1)
                y = round(random() * grid.height - grid.height / 2, 1)
                dots.append(Dot(x, y, "red"))
            grid.addDots(dots)

        enter = Button(self, text="Добавить точки", command=dot)
        helpLabel.grid(row=0, column=0)
        entry.grid(row=1, column=0)
        enter.grid(row=2, column=0)

    # функция добавления точек из файла
    @staticmethod
    def importDotsFromFile(grid):
        filename = askopenfilename(filetypes=(("TXT Files", "*.txt"), ("All files", "*.*")))
        f = open(filename, "r")
        dots = []
        for line in f.readlines():
            x, y = map(float, line.split())
            dots.append(Dot(x, y, "red"))
        grid.addDots(dots)

    # функция показа точек
    def showDots(self, grid):
        self.clear(grid)
        scr = Scrollbar(self)
        list = Listbox(self, yscrollcommand=scr.set, height=35)
        for line in [str(i.x) + " " + str(i.y) for i in grid.dots]:
            list.insert(END, line)
        scr.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, fill=BOTH)
        scr.config(command=list.yview)

    # функция записи точек в файл
    def writeDotsToFile(self, grid):
        self.clear(grid)
        helpLabel = Label(self, text="Имя файла (файл будет находиться в папке проекта)")
        v = StringVar()
        v.set("output.txt")
        file_name = Entry(self, textvariable=v)

        def write():
            f = open(file_name.get(), "w")
            f.writelines([str(i.x) + " " + str(i.y) + "\n" for i in grid.dots])
            f.close()
            helpLabel["text"] = "Готово!"

        enter = Button(self, text="Записать в файл", command=write)
        helpLabel.grid(row=0, column=0)
        file_name.grid(row=1, column=0)
        enter.grid(row=2, column=0)

    # функция показа меню редактирования
    def showEditMenu(self, grid, dot):
        grid.selected_dot = dot
        grid.drawDots()
        ind = 0
        for child in self.winfo_children():
            if ind > 0:
                child.destroy()
            ind += 1
        if dot is None:
            return

        helpLabel = Label(self, text="Изменение параметров точки")
        inputX = Entry(self)
        inputY = Entry(self)
        inputX.insert(END, str(dot.x))
        inputY.insert(END, str(dot.y))

        def remove():
            del grid.dots[grid.dots.index(dot)]
            self.showEditMenu(grid, None)

        def apply():
            dot.x = float(inputX.get())
            dot.y = float(inputY.get())
            grid.drawDots()

        apply_button = Button(self, text="Применить", command=apply)
        remove_button = Button(self, text="Удалить точку", command=remove, background="red")
        helpLabel.grid(row=1, column=0)
        inputX.grid(row=2, column=0)
        inputY.grid(row=3, column=0)
        apply_button.grid(row=4, column=0)
        remove_button.grid(row=5, column=0)

    # функция определения точек для редактирования
    def editDots(self, grid):
        self.clear(grid)

        def onMotion(event):
            x = round((event.x - grid.width * grid.size / 2) / grid.size, 1)
            y = round((grid.height * grid.size / 2 - event.y) / grid.size, 1)
            dot = grid.findDot(x, y)
            self.activeDot = dot
            if dot is None:
                grid.drawDots()
            else:
                grid.selectDot(dot.x, dot.y)

        def onCLick(event):
            if self.activeDot is not None:
                self.showEditMenu(grid, self.activeDot)
        grid.canvas.bind('<Motion>', onMotion)
        grid.canvas.bind('<Button-1>', onCLick)

        def unbind():
            grid.canvas.unbind('<Motion>')
            grid.canvas.unbind('<Button-1>')

        grid.canvas.bind('<Motion>', onMotion)
        button = Button(self, text="Завершить редактирование", command=unbind)
        button.grid(row=0, column=0)
