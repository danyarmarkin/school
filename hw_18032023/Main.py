from Tree import *
from tkinter import *

root = Tk("sd")
root.geometry("1080x720")
root.title("Calculator")

answer = Label(root, font=("Arial", 25))
answer.grid(row=1, column=1)

string_listener = StringVar()


def text_changed_callback(*args):
    global answer
    answer["text"] = calc(string_listener.get())


string_listener.trace("w", text_changed_callback)

entry = Entry(root, width=50, textvariable=string_listener)
Label(root, text="Expression").grid(row=0, column=0)
entry.grid(row=0, column=1)

Label(root, text="Answer:").grid(row=1, column=0)

# print("Answer:", calc(input("Expression: ")))

root.mainloop()
