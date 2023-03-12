import tkinter as tk
from tkinter import ttk
from LIB.navbar import *
from LIB.data_conn import *
from LIB.basicTree import *


class Students(ttk.LabelFrame):
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
        #DB Connection
        self.myDB = Database("AM.db")
        self.columnnames = self.myDB.get_fields("student")
        self.studentRecords = self.myDB.getAll("student")
        self.studentTree = MyTree(self.holdingFrame, self.columnnames, 0, 0)
        self.studentTree.Tree['show']='headings' #hide the id column
        self.studentTree.populateTree(self.studentRecords)

        #CRUD FUNCTIONS HERE
        self.crudFrame = ttk.LabelFrame(self.holdingFrame, text = "Database Operations: ")
        self.crudFrame.grid(row =1, column=0, **gridOptions)
        self.searchText = ttk.Label(self.crudFrame, text="Search: ")
        self.searchText.grid(row=0, column=0, **gridOptions)
        self.searchEntry = ttk.Entry(self.crudFrame)
        self.searchEntry.grid(row=0, column=1, **gridOptions)
        self.searchButton=ttk.Button(self.crudFrame, text="Search", command=None)
        self.searchButton.grid(row = 0, column=2, **gridOptions)
        self.deleteButton=ttk.Button(self.crudFrame, text="Delete", command = None)
        self.deleteButton.grid(row=0, column=3, **gridOptions)
        self.newButton = ttk.Button(self.crudFrame, text="New", command=None)
        self.newButton.grid(row=0, column=4, **gridOptions)

