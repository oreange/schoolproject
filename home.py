import tkinter as tk
from tkinter import ttk
from LIB.navbar import *
from LIB.basicTree import *
from LIB.data_conn import *


class Home(ttk.LabelFrame):
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
        #create a notebook and tabs/frames
        self.displayTabs = ttk.Notebook(self)
        self.displayTabs.grid(row=1, column=0, **gridOptions)
        self.tabOne = ttk.Frame(self.displayTabs, width=400, height = 200)
        # Treeview for tab one
        self.treeOne = MyTree(self.tabOne, ["Forename", "Surname", "Tutor Group", "Total"], 0, 0)
        self.treeOne.Tree['show'] = 'headings' #hide the id column of the treeview
        # Create a DB connection to get all results
        self.myDB = Database("AM.db")
        results = self.myDB.getAllScores()
        self.treeOne.populateTree(results)
        self.tabOne.grid(row=0, column=0, **gridOptions)
        self.displayTabs.add(self.tabOne, text = "Students performance: ")