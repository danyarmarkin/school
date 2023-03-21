from functools import partial
from tkinter import *
from math import sin, cos, pi


# структура точки
class Dot:
    x = 0
    y = 0
    color = "red"

    def __hash__(self):
        return hash(str(self.x) + str(self.y))

    def __init__(self, x, y, color="red"):
        self.x = x
        self.y = y
        self.color = color

    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


"""
class Grid
"""


class Grid:
    width = 30  # количество клеток по горизонтали
    height = 30  # количество клеток по вертикали
    size = 20  # размер ячейки
    frame = None
    canvas = None
    dots = []

    # перевод х
    def x(self, x):
        return x + self.width / 2

    # перевод у
    def y(self, y):
        return self.height / 2 - y

    def __init__(self, frame):
        self.frame = frame
        self.canvas = Canvas(self.frame)

    # рисование сетки
    def drawGrid(self):
        halfW = round(self.size * self.width / 2)
        halfH = round(self.size * self.height / 2)

        self.canvas.config(height=self.size * self.height, width=self.size * self.width)

        for i in range(0, self.size * (self.width + 0), self.size):
            self.canvas.create_line(i, 0, i, self.size * self.height, fill="#cccccc")
            self.canvas.create_text(i - self.size / 4,
                                    halfH + self.size / 4,
                                    text=str(int(i / self.size - self.width / 2)),
                                    font="Verdana 7")

        for i in range(0, self.size * (self.height + 0), self.size):
            self.canvas.create_line(0, i, self.size * self.width, i, fill="#cccccc")
            if i in [self.size * self.height / 2, 0]:
                continue
            self.canvas.create_text(halfW - self.size / 3,
                                    i + self.size / 4,
                                    text=str(int(-i / self.size + self.width / 2)),
                                    font="Verdana 7")

        self.canvas.pack()

    # рисование осей
    def drawAxis(self):
        halfW = round(self.size * self.width / 2)
        halfH = round(self.size * self.height / 2)
        self.canvas.create_line(0, halfH, halfW * 2, halfH, arrow=LAST, width=2)  # ox
        self.canvas.create_line(halfW, 2, halfW, halfH * 2, arrow=FIRST, width=2)  # oy
        self.canvas.create_text(halfW * 2 - self.size / 2, halfH + self.size / 2, text="x")
        self.canvas.create_text(halfW - self.size / 2, self.size / 2, text="y")

    # нарисовать / перерисовать точки
    def drawDots(self):
        self.canvas.delete("all")
        self.drawGrid()
        self.drawAxis()
        r = 3
        for dot in self.dots:
            self.canvas.create_oval(self.x(dot.x) * self.size - r,
                                    self.y(dot.y) * self.size - r,
                                    self.x(dot.x) * self.size + r,
                                    self.y(dot.y) * self.size + r,
                                    fill=dot.color)

    # добавление точки
    def addDot(self, dot):
        self.dots.append(dot)
        self.drawDots()

    # добавление массива точек
    def addDots(self, dots):
        self.dots += dots
        self.drawDots()

    # удалить все точки
    def clear(self):
        self.dots = []
        self.drawDots()

    def line(self, d1, d2):
        self.canvas.create_line(self.x(d1.x) * self.size,
                                self.y(d1.y) * self.size,
                                self.x(d2.x) * self.size,
                                self.y(d2.y) * self.size,
                                fill="green")


"""
==========================================================================================
************************************PROGRAM***********************************************
==========================================================================================
"""

root = Tk()
root.geometry("1080x720")
root.title("Matrix rotation                             help we are kept in bondage")

panel = Frame(root)
panel.grid(row=0, column=0)

grid_frame = Frame(root)
grid_frame.config(width=200, height=200)
grid = Grid(grid_frame)
grid.drawGrid()
grid.drawAxis()
grid_frame.place(x=400, y=50)

x1 = IntVar()
x1.set(1)
x2 = IntVar()
x2.set(4)
x3 = IntVar()
x3.set(6)
y1 = IntVar()
y1.set(1)
y2 = IntVar()
y2.set(5)
y3 = IntVar()
y3.set(3)
angle = IntVar()
w = 7
p1 = Frame(root)
l = Label(root)

def create_and_rotate(b):
    global p1, l
    grid.clear()
    d1 = Dot(x1.get(), y1.get())
    d2 = Dot(x2.get(), y2.get())
    d3 = Dot(x3.get(), y3.get())
    grid.addDots([d1, d2, d3])

    a = angle.get() * 0.01 * pi
    r_m = [
        [cos(a), sin(a)],
        [-sin(a), cos(a)]
    ]
    p1.destroy()
    p1 = Frame(root)
    p1.grid(row=3, column=0)
    l.destroy()
    l = Label(root, text="Матрица поворота на " + str(angle.get() * 0.01)[:5] + " * pi")
    l.grid(row=2, column=0)
    Label(p1, text=str(r_m[0][0])[:6]).grid(row=1, column=0)
    Label(p1, text=str(r_m[0][1])[:6]).grid(row=1, column=1)
    Label(p1, text=str(r_m[1][0])[:6]).grid(row=2, column=0)
    Label(p1, text=str(r_m[1][1])[:6]).grid(row=2, column=1)
    x_1 = x1.get() * r_m[0][0] + y1.get() * r_m[1][0]
    y_1 = x1.get() * r_m[0][1] + y1.get() * r_m[1][1]
    x_2 = x2.get() * r_m[0][0] + y2.get() * r_m[1][0]
    y_2 = x2.get() * r_m[0][1] + y2.get() * r_m[1][1]
    x_3 = x3.get() * r_m[0][0] + y3.get() * r_m[1][0]
    y_3 = x3.get() * r_m[0][1] + y3.get() * r_m[1][1]
    d_1 = Dot(x_1, y_1)
    d_2 = Dot(x_2, y_2)
    d_3 = Dot(x_3, y_3)
    grid.addDots([d_1, d_2, d_3])

    grid.line(d1, d2)
    grid.line(d2, d3)
    grid.line(d1, d3)
    grid.line(d_1, d_2)
    grid.line(d_2, d_3)
    grid.line(d_1, d_3)

    Label(p1, text="Итоговые координаты").grid(row=3, column=0)
    Label(p1, text=str(x_1)[:6]).grid(row=4, column=0)
    Label(p1, text=str(y_1)[:6]).grid(row=4, column=1)
    Label(p1, text=str(x_2)[:6]).grid(row=5, column=0)
    Label(p1, text=str(y_2)[:6]).grid(row=5, column=1)
    Label(p1, text=str(x_3)[:6]).grid(row=6, column=0)
    Label(p1, text=str(y_3)[:6]).grid(row=6, column=1)


Label(panel, text="Исходная фигура (х, у)").grid(row=0, column=0)
Entry(panel, textvariable=x1, width=w).grid(row=1, column=0)
Entry(panel, textvariable=y1, width=w).grid(row=1, column=1)
Entry(panel, textvariable=x2, width=w).grid(row=2, column=0)
Entry(panel, textvariable=y2, width=w).grid(row=2, column=1)
Entry(panel, textvariable=x3, width=w).grid(row=3, column=0)
Entry(panel, textvariable=y3, width=w).grid(row=3, column=1)
Button(panel, text="OK", command=partial(create_and_rotate, 0)).grid(row=4, column=1)

r_panel = Frame(root)
r_panel.grid(row=1, column=0)
Label(r_panel, text="Угол поворота [0; 2 * pi]").grid(row=5, column=0)
Scale(r_panel, from_=0, to=200, orient=HORIZONTAL, length=250, variable=angle, showvalue=FALSE,
      command=create_and_rotate).grid(row=6, column=0)


create_and_rotate(0)
root.mainloop()
