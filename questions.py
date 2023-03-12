import tkinter as tk
from tkinter import ttk
from LIB.navbar import *
from LIB.data_conn import *
from LIB.basicTree import *


class Questions(ttk.LabelFrame):
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

        self.holdingFrame = ttk.Frame(self)
        self.holdingFrame.grid(row=1, column=0, **gridOptions)
        self.myDB = Database("AM.db")
        self.topics = self.myDB.getAll("Topics")
        self.column_name = self.myDB.get_fields("questions")
        self.searchVar = tk.StringVar()
        self.searchDropDown = ttk.OptionMenu(self.holdingFrame,
                                             self.searchVar,
                                             self.topics[0][0],
                                             *self.topics)
        self.searchDropDown.grid(row=0, column=0, **gridOptions)
        self.filterButton = ttk.Button(self.holdingFrame, text="Filter", command = self.filter)
        self.filterButton.grid(row=0, column=1, **gridOptions)

        self.questionsTree = MyTree(self.holdingFrame, self.column_name, 1, 0)
        self.questionsTree.Tree['show']='headings'
        self.questionsTree.populateTree(self.myDB.getAll("questions"))

    def filter(self):
        topic = self.searchVar.get()
        self.questionsTree.Tree.delete(*self.questionsTree.Tree.get_children())
        questions = self.myDB.generalSQL(f"select * from questions where topic='{topic}'")
        self.questionsTree.populateTree(questions)