import time
import tkinter


class TestRoot(tkinter.Tk):
    questions = []
    current = -1
    true_answers = 0
    answers = []
    name = ""

    def __init__(self):
        super().__init__()
        self.geometry("800x400")
        self.title("Test")
        f = open("data.txt", "r")
        for i in f.readlines():
            q, a = map(str, i.replace("\n", "").split("_"))
            self.questions.append(Question(q, a))
            print(q, a)
        self.next_question()

    def next_question(self):
        self.current += 1

        for i in self.winfo_children():
            i.destroy()

        if self.current == len(self.questions):
            result_label = tkinter.Label(self, text=f"Ваш результат {self.true_answers} / {len(self.questions)}. "
                                                    f"Результат сохранен в файл с вашим именем")
            result_label.grid(row=0, column=0)
            f = open(f"{self.name}.txt", "w")
            for i, r in enumerate(self.answers):
                tkinter.Label(self, text=str(i + 1)).grid(row=i+1, column=0)
                tkinter.Label(self, text=(lambda: "Верно" if r else "Неверно")(),
                              bg=(lambda: "green" if r else "red")()).grid(row=i + 1, column=1)
            f.writelines([f"{i} {r}\n" for i, r in enumerate(self.answers)])
            return

        question = self.questions[self.current]
        question_label = tkinter.Label(self, text=question.question)
        answer_entry = tkinter.Entry(self)

        def checkAnswer():
            if answer_entry.get() == question.answer:
                question_label["text"] = "Правильно!"
                self.true_answers += 1
                self.answers.append(True)
            else:
                question_label["text"] = "Неверно!"
                self.answers.append(False)
            question_label.update()
            time.sleep(1.5)
            self.next_question()
        send = tkinter.Button(self, text="Проверить", command=checkAnswer)

        question_label.grid(row=0, column=0)
        answer_entry.grid(row=1, column=0)
        send.grid(row=2, column=0)


class Question:
    question = ""
    answer = ""

    def __init__(self, q, a):
        self.question = q
        self.answer = a

    def __str__(self):
        return self.question
