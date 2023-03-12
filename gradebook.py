import tkinter as tk
from tkinter import ttk
from LIB.navbar import *
from LIB.myList import *
from LIB.data_conn import *
from LIB.basicTree import *


class GradeBook(ttk.LabelFrame):
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
        self.studentLabelFrame = ttk.LabelFrame(self, text="Student Details: ")
        self.studentLabelFrame.grid(row=1, column=0, **gridOptions)
        #list box for all students
        self.DB = Database("AM.db")
        self.students = self.DB.getAll("student")
        self.studentList = ListWidget(self.studentLabelFrame, 0, 0)
        self.studentList.fillList(self.students)
        #view grades buttons
        self.viewGradesButons = ttk.Button(self.studentLabelFrame, text = "View Grades", command = self.viewGrades)
        self.viewGradesButons.grid(row = 1, column = 0, **gridOptions)

    def viewGrades(self):
        student = self.studentList.getSlected(evt=None)
        new_student = student.split(",")
        self.resultsFrame = ttk.LabelFrame(self, text=f"{new_student[1]} {new_student[2]} Grades")
        self.resultsFrame.grid(row=2, column=0, pady=5, padx=5, sticky=tk.NSEW, rowspan=3)
        self.resultTree=MyTree(self.resultsFrame,["Student ID","Test Name", "Topic", "Difficulty", "Date", "Score"], 0, 0)
        resultsData = self.DB.getStudentGrades(new_student[0])
        self.resultTree.populateTree(resultsData)