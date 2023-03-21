from tkinter import *
from task import *


class Grid:
    width = 30  # количество клеток по горизонтали
    height = 30  # количество клеток по вертикали
    size = 20  # размер ячейки
    frame = None
    canvas = None
    dots = []
    selected_dot = None

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

    # найти ближайшую точку
    def findDot(self, x, y):
        m = 10 ** 5
        d = None
        for dot in self.dots:
            r = (dot.x - x) ** 2 + (dot.y - y) ** 2
            if r < m:
                m = r
                d = dot
        if m >= 0.7:
            return None
        return d

    # выбрать точку
    def selectDot(self, x, y):
        self.canvas.delete("all")
        self.drawGrid()
        self.drawAxis()

        for dot in self.dots:
            r = 3
            color = dot.color
            if dot.x == x and dot.y == y:
                r = 5
                color = "blue"
            self.canvas.create_oval(self.x(dot.x) * self.size - r,
                                    self.y(dot.y) * self.size - r,
                                    self.x(dot.x) * self.size + r,
                                    self.y(dot.y) * self.size + r,
                                    fill=color)

    # нарисовать / перерисовать точки
    def drawDots(self):
        if self.selected_dot is not None:
            self.selectDot(self.selected_dot.x, self.selected_dot.y)
            return
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

    # отобразить решение задачи
    def solutions(self):
        task = Task(self.dots)
        triangles = task.prepareTriangles()
        dots = task.getDots(triangles)
        res_triangles = []

        for triangle in triangles:
            d1 = triangle.dots[0]
            d2 = triangle.dots[1]
            d3 = triangle.dots[2]
            if dots[d1] >= 2:
                res_triangles.append(triangle)
                continue
            if dots[d2] >= 2:
                res_triangles.append(triangle)
                continue
            if dots[d3] >= 2:
                res_triangles.append(triangle)
                continue

        for triangle in res_triangles:
            print(triangle)
            d1 = triangle.dots[0]
            d2 = triangle.dots[1]
            d3 = triangle.dots[2]
            self.canvas.create_line(self.x(d1.x) * self.size,
                                    self.y(d1.y) * self.size,
                                    self.x(d2.x) * self.size,
                                    self.y(d2.y) * self.size,
                                    fill="green")
            self.canvas.create_line(self.x(d1.x) * self.size,
                                    self.y(d1.y) * self.size,
                                    self.x(d3.x) * self.size,
                                    self.y(d3.y) * self.size,
                                    fill="green")
            self.canvas.create_line(self.x(d3.x) * self.size,
                                    self.y(d3.y) * self.size,
                                    self.x(d2.x) * self.size,
                                    self.y(d2.y) * self.size,
                                    fill="green")
