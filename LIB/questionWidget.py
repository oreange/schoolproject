import tkinter as tk
from tkinter import ttk
from LIB.data_conn import *

class Question():

    def __init__(self, parent, q_id, question,answer,r, c):
        self.parent = parent
        self.q_id = q_id
        self.question = question
        self.answer = answer
        self.r = r
        self.c = c
        self.holdingFrame = ttk.Frame(self.parent)
        self.holdingFrame.grid(row = r, column = c, padx=5, pady=5, sticky=tk.W)
        self.questionText = ttk.Label(self.holdingFrame, text="Question")
        self.questionText.grid(row = 0, column=0, padx=5, pady=5, sticky=tk.W)
        self.questionWidget = ttk.Entry(self.holdingFrame)
        self.questionWidget.insert(0, self.question)
        self.questionWidget.grid(row = 1, column = 0,padx=5, pady=5, sticky=tk.W)
        self.answerText = ttk.Label(self.holdingFrame, text = "Answer")
        self.answerText.grid(row = 0, column = 1, pady=5, padx=5, sticky=tk.W)
        self.answerWidget = ttk.Entry(self.holdingFrame)
        self.answerWidget.insert(0, self.answer)
        self.answerWidget.grid(row = 1, column=1,padx=5, pady=5, sticky=tk.W)

        self.removeButton = ttk.Button(self.holdingFrame, text = "-", command = lambda x = self.q_id:self.removeQuestion(x))
        self.removeButton.grid(row = 1, column=2, padx=5, pady=5, sticky=tk.W)

    def removeQuestion(self, id):
        self.holdingFrame.destroy()
        db = Database("AM.db")
        db.removeQuestion(id)


if __name__=="__main__":
    win = tk.Tk()
    q1 = Question(win, "Capital of ireland", "Dublin", 0, 0)
    win.mainloop()