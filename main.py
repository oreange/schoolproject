import tkinter as tk
from tkinter import ttk
from home import *
from test import *
from gradebook import *
from editTest import *
from newTest import *
from students import *
from logOn import *
from studentHome import *
from studentGradeBook import *
from questions import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.frames = [Home(self,
                            "Home"),
                       Test(self,
                            "Tests"),
                       GradeBook(self,
                                 "Gradebook"),
                       Students(self,
                                "Students"),
                       Questions(self,
                                 "Question Bank"),
                       EditTest(self,
                                "Edit Test"),
                       NewTest(self,
                               "Create a New Test"),
                       LogOn(self)
                       ]

        self.studentFrames=[StudentHome(self,
                                        "Student Menu"),
                            StudentGrade(self,
                                         "My Grades")]
        self.show_frame(7)

    def show_frame(self, frame_num):
        frame_to_show = self.frames[frame_num]
        frame_to_show.tkraise()

    def show_student_frame(self, frame_num):
        frame_to_show = self.studentFrames[frame_num]
        frame_to_show.tkraise()


if __name__ == "__main__":
    myApp = App()
    myApp.mainloop()
