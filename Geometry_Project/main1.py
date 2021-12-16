from tkinter import *
from math import *
from tkinter import messagebox
from random import *
from functools import partial
from tkinter.filedialog import *

root = Tk()
root.title("Геометрия")
root.geometry("1200x600")

maxx = 640
maxy = 480
xmax = 10;
xmin = -10;
ymax = 10;
ymin = -10


def quit():
    global root
    res = messagebox.askyesno('Exit', 'Do you want to kill this window?')
    if res == True:
        root.destroy()


def coord(maxx, maxy):
    c.create_line(0, maxy / 2, maxx, maxy / 2, fill="black",
                  width=2, arrow=LAST, arrowshape="5 10 5")
    c.create_line(maxx / 2, 0, maxx / 2, maxy, fill="black",
                  width=2, arrow=FIRST, arrowshape="5 10 5")
    c.create_text(maxx - 8, maxy / 2 + 10, text='X', anchor=W, fill="black")
    c.create_text(maxx / 2 + 10, 5, text='Y', anchor=W, fill="black")
    c.create_text(maxx / 2 - 7, maxy / 2 + 7, text='0', anchor=W, fill="black")

    for i in range(1, -xmin + xmax):
        summ = -xmin + xmax
        if i != xmax:
            c.create_line(i * maxx / summ, 0, i * maxx / summ, maxy, fill="lightgrey",
                          width=1)
            c.create_line(0, i * maxy / summ, maxx, i * maxy / summ, fill="lightgrey",
                          width=1)
            c.create_text(i * maxx / summ, maxy / 2 + xmax, text=i - xmax, fill='black')
            c.create_text(maxx / 2 + 10, i * maxy / summ, text=-i - xmin, fill='black')
            c.create_line(i * maxx / summ, maxy / 2, i * maxx / summ, maxy / 2 + 5, fill="black",
                          width=1)
            c.create_line(maxx / 2, i * maxy / summ, maxx / 2 + 5, i * maxy / summ, fill="black",
                          width=1)


###################################################################### Random
def rand(root, pn_control, vid):
    txt = StringVar()

    ent = Entry(pn_control, textvariable=txt)
    ent.focus()
    ent.pack()
    enbutran = Button(pn_control, text='Ок', command=partial(tochr, txt, root, ent))
    enbutran.pack()


def tochr(txt, root, ent):
    i = int(txt.get())
    f = open('txt.txt', 'w')
    a = []
    for j in range(0, i):
        k = 0
        while k != 1:
            num = (str(round(uniform(-10, 10), 2)) + ' ' + str(round(uniform(-10, 10), 2)))
            if not (num in a):
                k += 1
                a.append(num)
    for j in a:
        f.write(j + '  ')
    f.close()

    drawt(root, 'txt.txt')


def drawt(root, file_dr):
    f = open(file_dr, 'r')
    spis = f.readlines()
    spis = spis[0].split('  ')
    spis.pop(-1)
    for j in range(0, len(spis)):
        spis[j] = (spis[j]).split(' ')
    for j in spis:
        c.create_oval(320 + 32 * float(j[0]), 240 - 24 * float(j[1]),
                      320 + 32 * float(j[0]), 240 - 24 * float(j[1]), width=3)


#############################################################################
#############################################################################Klava 
def klav(root, pn_control, vid):
    txt = StringVar()

    ent1 = Entry(pn_control, textvariable=txt)
    ent.focus()
    ent.pack()
    enbutran1 = Button(pn_control, text='Ок', command=partial(tochkl, txt, root, pn_control))
    enbutran.pack()
    vid.append(ent1, enbutran1)


def tochkl(txt, root, pn_control):
    pn_control.destroy()
    f = open('txt.txt', 'w')
    k = 1
    vvodcoord(root, pn_control, f, k, txt)


def vvodcoord(root, pn_control, f, k, txt):
    pn_control = Frame(root, height=120, width=640)
    pn_control.pack()
    txtx = StringVar()
    txty = StringVar()
    labx = Label(pn_control, text='x')
    entx = Entry(pn_control, textvariable=txtx)

    labx.pack()
    entx.pack()
    laby = Label(pn_control, text='y')
    laby.pack()
    enty = Entry(pn_control, textvariable=txty)
    enty.pack()
    enbutran = Button(pn_control, text='Ок', command=partial(zapinf, f,
                                                             txtx, txty, root, pn_control, k, txt))
    enbutran.pack()


def zapinf(f, txtx, txty, root, pn_control, k, txt):
    if k == int(txt.get()):
        f.write(str(txtx.get()) + ' ' + str(txty.get()) + '  ')
        pn_control.destroy()
        f.close()
        drawt(root, 'txt.txt')
    else:
        k += 1
        f.write(str(txtx.get()) + ' ' + str(txty.get()) + '  ')
        pn_control.destroy()
        vvodcoord(root, pn_control, f, k, txt)


########################################################################
########################################################################Mouse
def mousevv(root, c):
    c.bind('<Button-1>', clickdr)
    f = open('txt.txt', 'w')
    f.close()


def clickdr(event):
    c.create_oval(event.x, event.y, event.x, event.y, width=3)
    f = open('txt.txt', 'a')
    f.write(str((event.x - 320) * 10 / 320) + ' ' + str((240 - event.y) * 10 / 240) + '  ')


########################################################################    
########################################################################File v ek
def coord_file(root, c):
    filename = askopenfilename()
    drawt(root, filename)


def pr_f(root, pn_control):
    f = open('txt.txt', 'r')
    spis = f.readlines()
    spis = spis[0].split('  ')
    spis.pop(-1)
    s = ''''''
    for j in range(0, len(spis)):
        spis[j] = (spis[j]).split(' ')
    for j in spis:
        s += (j[0] + ',' + j[1] + '\n')
    lab = Label(pn_control, text=s)
    lab.pack()


########################################################################
########################################################################Clear


########################################################################
########################################################################

########################################################################
mainmenu = Menu(root)
root.config(menu=mainmenu)
pn_graph = Frame(root, height=480, width=640)
pn_graph.pack(side=RIGHT)
pn_control = Frame(root, height=120, width=640)
pn_control.pack()
c = Canvas(pn_graph, height=480, width=640, bg='white')
c.pack(fill='both', expand=1)
coord(maxx, maxy)
vid = []


########################################################################Clear
def ochist(root):
    c.delete("all")
    coord(maxx, maxy)
    vid = []


########################################################################
########################################################################
filemenu1 = Menu(mainmenu, tearoff=0)
filemenu1.add_command(label="Клавиатура", command=partial(klav, root, pn_control, vid))
filemenu1.add_command(label="Мышь", command=partial(mousevv, root, c))
filemenu1.add_command(label="Файл", command=partial(coord_file, root, c))
filemenu1.add_command(label="Random", command=partial(rand, root, pn_control, vid))

filemenu2 = Menu(mainmenu, tearoff=0)
filemenu2.add_command(label="Файл", command=partial(coord_file, root, c))
filemenu2.add_command(label="Экран", command=partial(pr_f, root, pn_control))
filemenu3 = Menu(mainmenu, tearoff=0)
filemenu3.add_command(label="Очистить экран", command=partial(ochist, root))
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Ввод",
                     menu=filemenu1)
mainmenu.add_cascade(label="Вывод",
                     menu=filemenu2)
mainmenu.add_cascade(label="Редактирование", menu=filemenu3)
mainmenu.add_cascade(label="Вычисление")
mainmenu.add_cascade(label="Демонстрация")
mainmenu.add_cascade(label="Справка", menu=helpmenu)
mainmenu.add_command(label="Выход", command=quit)

root.config(menu=mainmenu)

root.mainloop()
#######################Не доделана очистака, возникла проблема, если всё делать без глбальных переменных
