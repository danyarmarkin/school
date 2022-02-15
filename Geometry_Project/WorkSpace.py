from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename

from figures import *
from random import random


class WorkSpace(Frame):

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
        button = Button(self, text="Stop mouse binding", command=unbind)
        button.grid(row=0, column=0)
        color.grid(row=1, column=0)

    def addDotWithKeyboard(self, grid):
        self.clear(grid)
        helpLabel = Label(self, text="Add coordinates with keyboard X, Y")
        inputX = Entry(self)
        inputY = Entry(self)

        def dot():
            grid.addDot(Dot(float(inputX.get()), float(inputY.get()), "red"))

        enter = Button(self, text="Add dot", command=dot)
        helpLabel.grid(row=0, column=0)
        inputX.grid(row=1, column=0)
        inputY.grid(row=2, column=0)
        enter.grid(row=3, column=0)

    def addDotWithRandom(self, grid):
        self.clear(grid)
        helpLabel = Label(self, text="Add amounts of dots")
        entry = Entry(self)

        def dot():
            n = int(entry.get())
            dots = []
            for _ in range(n):
                x = round(random() * grid.width - grid.width / 2, 1)
                y = round(random() * grid.height - grid.height / 2, 1)
                dots.append(Dot(x, y, "red"))
            grid.addDots(dots)

        enter = Button(self, text="Add dot", command=dot)
        helpLabel.grid(row=0, column=0)
        entry.grid(row=1, column=0)
        enter.grid(row=2, column=0)

    @staticmethod
    def importDotsFromFile(grid):
        filename = askopenfilename(filetypes=(("TXT Files", "*.txt"), ("All files", "*.*")))
        f = open(filename, "r")
        dots = []
        for line in f.readlines():
            x, y = map(float, line.split())
            dots.append(Dot(x, y, "red"))
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
        file_name = Entry(self, textvariable=v)

        def write():
            f = open(file_name.get(), "w")
            f.writelines([str(i.x) + " " + str(i.y) + "\n" for i in grid.dots])
            f.close()
            helpLabel["text"] = "Done!"

        enter = Button(self, text="Write", command=write)
        helpLabel.grid(row=0, column=0)
        file_name.grid(row=1, column=0)
        enter.grid(row=2, column=0)

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

        helpLabel = Label(self, text="Change dot params")
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

        apply_button = Button(self, text="Apply", command=apply)
        remove_button = Button(self, text="Remove dot", command=remove)
        helpLabel.grid(row=1, column=0)
        inputX.grid(row=2, column=0)
        inputY.grid(row=3, column=0)
        apply_button.grid(row=4, column=0)
        remove_button.grid(row=5, column=0)

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
        button = Button(self, text="Stop mouse binding", command=unbind)
        button.grid(row=0, column=0)
