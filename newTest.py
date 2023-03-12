import tkinter as tk
from tkinter import ttk
from LIB.navbar import *
from LIB.data_conn import *
from LIB.myList import *
from LIB.questionWidget import *
from tkinter import messagebox


class NewTest(ttk.LabelFrame):
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
        #Create a frame to hold new test widgets
        self.newTestFrame = tk.LabelFrame(self, text = "Test Details: ")
        self.newTestFrame.grid(row = 1, column=0, **gridOptions)
        #Test name label
        self.testName = ttk.Label(self.newTestFrame, text = "Test Name: ")
        self.testName.grid(row = 0, column=0, **gridOptions)
        self.testNameEntry = ttk.Entry(self.newTestFrame)
        self.testNameEntry.grid(row=0, column=1, **gridOptions)
        #Duration label & wid
        self.durationLabel = ttk.Label(self.newTestFrame, text = "Duration: ")
        self.durationLabel.grid(row=1, column=0, **gridOptions)
        self.durationEntry = ttk.Entry(self.newTestFrame)
        self.durationEntry.grid(row=1, column=1, **gridOptions)
        #difficulty option menu & assoc wids
        self.difficultlyLabel = ttk.Label(self.newTestFrame, text = "Difficullty: ")
        self.difficultlyLabel.grid(row = 2, column=0, **gridOptions)
        #connect to db & get difficulty data
        self.DB = Database("AM.db")
        self.difficultyData = self.DB.generalSQL("select level from difficulty")
        diff = [item[0] for item in self.difficultyData]
        self.difficultyOptionVar = tk.StringVar(self.newTestFrame)
        self.difficultyOptionMenu = ttk.OptionMenu(self.newTestFrame, self.difficultyOptionVar,diff[0],
                                                   *diff)
        self.difficultyOptionMenu.grid(row = 2, column=1, **gridOptions)
        #Topic option menu and wids
        self.topicLabel = ttk.Label(self.newTestFrame, text="Topic: ")
        self.topicLabel.grid(row=3, column=0, **gridOptions)
        self.topicVar = tk.StringVar(self.newTestFrame)
        self.topicData = self.DB.generalSQL("select topic from topics")
        topic = [item[0] for item in self.topicData]
        self.topicOptionMenu = ttk.OptionMenu(self.newTestFrame, self.topicVar,
                                              topic[0],*topic)
        self.topicOptionMenu.grid(row = 3, column=1, **gridOptions)

        #save test button & functionality
        self.saveButton = ttk.Button(self.newTestFrame, text = "Save", command = self.saveTest)
        self.saveButton.grid(row=4, column=0, **gridOptions)

        #add questions button
        self.addQuestionsButton = ttk.Button(self.newTestFrame, text = "Add Questions", command=self.addQuestion)
        self.addQuestionsButton.grid(row = 4, column=1, ** gridOptions)
        self.addQuestionsButton.state(['disabled'])

        self.addQuestionFrame = ttk.LabelFrame(self, text = "Available Questions: ")
        self.addQuestionFrame.grid(row = 2, column=0,**gridOptions)
        self.questionsFrame = ttk.LabelFrame(self, text = "Questions on test")
        self.questionsFrame.grid(row=1, column=1, rowspan = 2,**gridOptions)
        self.q_row, self.q_col = 0, 0

        self.questionsToAdd = []

    def saveTest(self):
        values = [self.testNameEntry.get(), self.durationEntry.get(),
                self.difficultyOptionVar.get(),self.topicVar.get()]
        if values[0]and values[1] and values[2]and values[3]:
            self.DB.addRecord("test", values)
            messagebox.showinfo("Test Added", "New test has been added to the database")
            self.testNameEntry.configure(state='disabled')
            self.durationEntry.configure(state='disabled')
            self.saveButton.state(['disabled'])
            self.addQuestionsButton.state(['!disabled'])
        else:
            messagebox.showinfo("Incomplete Data", "Please complete all elements of the form")

    def addQuestion(self):
        self.questions = self.DB.generalSQL(f"select * from questions where topic ='{self.topicVar.get()}'")
        self.questionList = ListWidget(self.addQuestionFrame,0,0)
        self.questionList.fillList(self.questions)
        self.addButton = ttk.Button(self.addQuestionFrame, text="Add Selected", command = self.populateQuestionFrame)
        self.addButton.grid(row = 1, column = 0, pady=5, padx=5, sticky=tk.W)
        self.createNewButton = ttk.Button(self.addQuestionFrame, text = "Add New Question",
                                          command=self.addNewQuestion)
        self.createNewButton.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.saveTestButton = ttk.Button(self.addQuestionFrame, text="Save Test",
                                         command=self.saveTestAll)
        self.saveTestButton.grid(row = 1, column=2, pady=5, padx=5, sticky=tk.W)

    def populateQuestionFrame(self):
        q = self.questionList.getSlected(evt=None)
        new_q = q.split(",")
        self.questionsToAdd.append(new_q[0])
        Question(self.questionsFrame, new_q[0],new_q[1],
                 new_q[2],self.q_row, self.q_col)
        self.q_row+=1

    def saveTestAll(self):
        #get the test ID
        test_id = self.DB.generalSQL("select max(testid) from test")
        if test_id:
            for i in range(0, len(self.questionsToAdd)):
                self.DB.addData("test_parts", (test_id[0][0],self.questionsToAdd[i]))
            messagebox.showinfo("Test Created", "Questions Successfully added to test")
        self.window.frames[1].testList.fillList(self.DB.generalSQL("select * from test"))

    def addNewQuestion(self):
        new_window = tk.Toplevel(self)
        questionLabel = ttk.Label(new_window, text ="Question: ")
        questionLabel.grid(row=0, column = 0, padx=5, pady=5, sticky=tk.W)
        self.questionEntry = ttk.Entry(new_window)
        self.questionEntry.grid(row = 0, column = 1, padx=5, pady=5, sticky=tk.W)
        answerLabel = ttk.Label(new_window, text = "Answer: ")
        answerLabel.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.answerEntry=ttk.Entry(new_window)
        self.answerEntry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        addButton =ttk.Button(new_window, text = "Add", command = self.saveNewQuestion)
        addButton.grid(row=2, column=0,padx=5, pady=5, sticky=tk.W)
        closeButton = ttk.Button(new_window, text = "Close", command = new_window.destroy)
        closeButton.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)
        new_window.mainloop()

    def saveNewQuestion(self):
        self.questionList.insert(tk.END, "test")
        if self.questionEntry.get() and self.answerEntry.get():
            print(self.questionEntry.get())
            self.DB.addRecord("questions", (self.questionEntry.get(),
                                            self.answerEntry.get(),
                                            self.topicVar.get()))
            new_q = self.DB.generalSQL("select max(questionID) from questions")
            all_questions = self.DB.generalSQL(f"select * from questions where topic='{self.topicVar.get()}'")
            self.questionList.fillList(all_questions)
            messagebox.showinfo("Question Added", "Question successfully added")
            self.questionEntry.delete(0, tk.END)
            self.answerEntry.delete(0, tk.END)


if __name__ =="__main__":
    win = tk.Tk()
    newT = NewTest(win, "Create a new test: ")
    win.mainloop()
