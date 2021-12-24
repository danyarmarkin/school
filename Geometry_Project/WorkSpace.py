from functools import partial
from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename

from figures import *
from random import random


class WorkSpace(Frame):


    def clear(self, grid):
        grid.canvas.unbind('<Button-1>')
        grid.canvas.unbind('<Motion>')
        grid.drawDots()
        for child in self.winfo_children():
            child.destroy()
        self.config(width=400, height=720)

    def __init__(self, root):
        super().__init__(root)
        self.config(width=400, height=720)

    def addDotsWithMouse(self, grid):
        self.clear(grid)
        def onClick(event):
            x = round((event.x - grid.width * grid.size / 2) / grid.size, 1)
            y = round((grid.height * grid.size / 2 - event.y) / grid.size, 1)
            print(x, y)
            grid.addDot(Dot(x, y))

        def unbind():
            grid.canvas.unbind('<Button-1>')

        grid.canvas.bind('<Button-1>', onClick)
        button = Button(self, text="Stop mouse binding", command=unbind)
        button.grid(row=0, column=0)

    def addDotWithKeyboard(self, grid):
        self.clear(grid)
        helpLabel = Label(self, text="Add coordinates with keyboard X, Y")
        inputX = Entry(self)
        inputY = Entry(self)

        def dot():
            grid.addDot(Dot(float(inputX.get()), float(inputY.get())))

        enter = Button(self, text="Add dot", command=dot)
        helpLabel.grid(row=0, column=0)
        inputX.grid(row=1, column=0)
        inputY.grid(row=2, column=0)
        enter.grid(row=3, column=0)

    def addDotWithRandom(self, grid):
        self.clear(grid)
        helpLabel = Label(self, text="Add amounts of dots")
        input = Entry(self)

        def dot():
            n = int(input.get())
            dots = []
            for _ in range(n):
                x = round(random() * grid.width - grid.width / 2, 1)
                y = round(random() * grid.height - grid.height / 2, 1)
                dots.append(Dot(x, y))
            grid.addDots(dots)

        enter = Button(self, text="Add dot", command=dot)
        helpLabel.grid(row=0, column=0)
        input.grid(row=1, column=0)
        enter.grid(row=2, column=0)

    def importDotsFromFile(self, grid):
        filename = askopenfilename(filetypes=(("TXT Files", "*.txt"), ("All files", "*.*")))
        f = open(filename, "r")
        dots = []
        for line in f.readlines():
            x, y = map(float, line.split())
            dots.append(Dot(x, y))
        grid.addDots(dots)

    def showDots(self, grid):
        self.clear(grid)
        text = ""
        for line in [str(i.x) + " " + str(i.y) + "\n" for i in grid.dots]:
            text += line
        scroll = scrolledtext.ScrolledText(self, width=200, height=700)
        scroll.insert(INSERT, text)
        scroll.configure(state='disabled')
        scroll.grid(row=0, column=0)

    def writeDotsToFile(self, grid):
        self.clear(grid)
        helpLabel = Label(self, text="File name")
        v = StringVar()
        v.set("output.txt")
        input = Entry(self, textvariable=v)

        def write():
            f = open(input.get(), "w")
            f.writelines([str(i.x) + " " + str(i.y) + "\n" for i in grid.dots])
            f.close()
            helpLabel["text"] = "Done!"

        enter = Button(self, text="Write", command=write)
        helpLabel.grid(row=0, column=0)
        input.grid(row=1, column=0)
        enter.grid(row=2, column=0)

    def editDots(self, grid):
        self.clear(grid)

        pre = 0
        def onMotion(event):
            x = round((event.x - grid.width * grid.size / 2) / grid.size, 1)
            y = round((grid.height * grid.size / 2 - event.y) / grid.size, 1)
            dot = grid.findDot(x, y)
            print(x, y)
            print(dot)
            if dot is None:
                grid.drawDots()
            else:
                print("find")
                grid.selectDot(dot.x, dot.y)

        grid.canvas.bind('<Motion>', onMotion)


        def unbind():
            grid.canvas.unbind('<Motion>')

        grid.canvas.bind('<Motion>', onMotion)
        button = Button(self, text="Stop mouse binding", command=unbind)
        button.grid(row=0, column=0)

