import tkinter as tk
from tkinter import ttk
from LIB.studentNavBar import *

class StudentHome(ttk.LabelFrame):
    def __init__(self, window, title):
        super().__init__(window)
        self.window = window
        self.title = title
        self['text'] = self.title

        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.NSEW}
        self.grid(row = 0, column = 0, **gridOptions)
        self.nav = StudentNavBar(self.window, self)