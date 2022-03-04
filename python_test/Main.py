from test_root import *

root = tkinter.Tk()
root.title("Test")
root.geometry("600x400")

title = tkinter.Label(root, text="Тест")
name_title = tkinter.Label(root, text="Ваше имя")
name = tkinter.Entry(root)
name.insert(tkinter.END, "Иван")


def start():
    test_root = TestRoot()
    test_root.name = name.get()
    test_root.mainloop()


start = tkinter.Button(root, text="Начать", command=start)

title.grid(row=0, column=1)
name_title.grid(row=1, column=0)
name.grid(row=2, column=0)
start.grid(row=3, column=2)


root.mainloop()
