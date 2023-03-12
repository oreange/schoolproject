import tkinter as tk
from tkinter import ttk
from LIB.data_conn import *
from LIB.questionWidget import *
from LIB.navbar import *

class EditTest(ttk.LabelFrame):
    """A class to create frame objects used in an App"""
    def __init__(self, window, title):
        super().__init__(window)
        self.window = window
        self.title = title
        self['text'] = self.title
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.NSEW}
        self.grid(row = 0, column = 0, **gridOptions)
        #Create an instance of the nav bar
        self.navigation = NavBar(self.window, self)
        self.itemFrame = ttk.Frame(self)
        self.itemFrame.grid(row=1, column=1,sticky=tk.NSEW, pady=5, padx=5)
        self.DBconn = Database("AM.db")


    def populate(self, data, fields):
        self.data = data
        r, c=0,0
        for i in range(0, len(fields)):
            self.label = ttk.Label(self.itemFrame, text = fields[i])
            self.label.grid(row =r, column=c,padx=5, pady=5, sticky=tk.W)
            self.entryVar = tk.StringVar()
            self.entry = ttk.Entry(self.itemFrame)
            self.entry.insert(0,data[i])
            self.entry.grid(row=r, column=c+1, padx=5, pady=5, sticky=tk.W)
            r+=1
        self.addLabel = ttk.Label(self.itemFrame, text ="Add Questions:")
        self.addLabel.grid(row= r, column = c, pady=5, padx=5, sticky=tk.W)
        #Add questions option menu
        self.optionVar = tk.StringVar()
        self.questions = self.DBconn.getNewQuestions(data[4])
        self.addMenu = tk.OptionMenu(self.itemFrame, self.optionVar,self.questions[0], *self.questions)
        self.addMenu.configure(width=15)
        self.addMenu.grid(row = r, column = c+1, pady=5, padx=5, sticky=tk.W)
        #Add button
        self.addButton= ttk.Button(self.itemFrame, text = "+", command = self.addQuestions, width=5)
        self.addButton.grid(row = r, column=2, padx=5, pady=5, sticky=tk.W)

        self.questAns = self.DBconn.getQuestionAnswer(data[0])
        self.questionsFrame = ttk.LabelFrame(self.itemFrame, text="Questions in Test")
        self.questionsFrame.grid(row=0, column=3, pady=5,padx=5, sticky=tk.NSEW, rowspan=10)
        self.q_row, self.q_col = 0, 0
        for q in self.questAns:
            Question(self.questionsFrame,q[0], q[1],q[2],self.q_row, self.q_col)
            self.q_row+=1

    def addQuestions(self):
        q = self.optionVar.get().strip(""" ,()'""" ).strip("'")
        new_q = q.split(",")
        Question(self.questionsFrame, new_q[0], new_q[1], new_q[2],self.q_row, self.q_col)
        self.q_row+=1
        #Make saves to DB
        self.DBconn.addData("test_parts", (self.data[0], new_q[0]))

    def goBack(self):
        #clear the holding fraem
        question_wids=self.itemFrame.winfo_children()
        for q in question_wids:
            q.destroy()
        self.window.show_frame(1)

