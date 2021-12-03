from tkinter import *


class Grid:
    width = 40
    height = 30
    size = 20
    frame = None
    canvas = None
    dots =[]

    def x(self, x):
        return x + self.width / 2

    def y(self, y):
        return self.height / 2 - y

    def __init__(self, frame):
        self.frame = frame
        self.canvas = Canvas(self.frame)

    def drawGrid(self):
        self.canvas.config(height=self.size * self.height, width=self.size*self.width)

        for i in range(self.size, self.size * (self.width + 1), self.size):
            self.canvas.create_line(i, 0, i, self.size*self.height)

        for i in range(self.size, self.size * (self.height + 1), self.size):
            self.canvas.create_line(0, i, self.size*self.width, i)

        self.canvas.pack()

    def drawAxis(self):
        halfW = round(self.size * self.width / 2)
        halfH = round(self.size * self.height / 2)
        print(halfW, halfH)
        self.canvas.create_line(0, halfH, halfW * 2, halfH, arrow=LAST, width=2)  # ox
        self.canvas.create_line(halfW, 0, halfW, halfH * 2, arrow=FIRST, width=2)  # oy

    def addDot(self, dot):
        self.dots.append(dot)
        self.drawDots()

    def clear(self):
        self.dots = []
        self.drawDots()

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
                                    fill="red")
