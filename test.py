import tkinter as tk
from tkinter import ttk
from LIB.navbar import *
from LIB.data_conn import *
from LIB.myList import *
from tkinter import messagebox


class Test(ttk.LabelFrame):
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
        #Frame to hold all widgets
        self.itemFrame = ttk.Frame(self)
        self.itemFrame.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        #Title Label
        self.titleLabel = ttk.Label(self.itemFrame, text = "Select a test:", font=("Arial", 14))
        self.titleLabel.grid(row = 0, column=0, pady=5,padx=5, sticky=tk.W, columnspan=2)
        #List box containing test
        #connect to DB and get the tests
        self.myDB_connection = Database("AM.db")
        self.tests = self.myDB_connection.getAll("test")
        self.fields = self.myDB_connection.get_fields("test")
        self.myDB_connection.connection.close()
        #create the list box
        self.testList = ListWidget(self.itemFrame,1,0)
        self.testList.fillList(self.tests)

        #Buttons
        self.editButton=ttk.Button(self.itemFrame, text ="View/Edit", command = self.openEditScreen)
        self.editButton.grid(row = 2, column=0, padx=5, pady=5, sticky=tk.EW)
        self.deleteTestButton = ttk.Button(self.itemFrame, text="Delete Test", command = self.deleteTest)
        self.deleteTestButton.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)
        self.newTestButton = ttk.Button(self.itemFrame, text = "New Test", command=self.newTest)
        self.newTestButton.grid(row = 2, column=2, padx=5, pady=5, sticky=tk.EW)

    def openEditScreen(self):
        item = self.testList.getSlected(evt=None)
        #convert item into list
        new_item = item.split(",")
        self.window.show_frame(5)
        self.window.frames[5].populate(new_item, self.fields)

    def deleteTest(self):
        record = self.testList.getSlected(evt=None)
        new_record = record.split(",")
        if new_record:
            self.myDB_connection = Database("AM.db")
            self.myDB_connection.deleteRecord("testid", "test_parts", new_record[0])
            self.myDB_connection.deleteRecord("testID", "test", new_record[0])
            self.testList.fillList(self.myDB_connection.generalSQL("select * from test"))
            messagebox.showinfo("Deletion", "Test deleted from system")
        else:
            messagebox.showinfo("Alert", "Select a test to be deleted")

    def newTest(self):
        for widgets in self.window.frames[6].addQuestionFrame.winfo_children():
            widgets.destroy()
        for widgets in self.window.frames[6].questionsFrame.winfo_children():
            widgets.destroy()
        self.window.frames[6].testNameEntry.configure(state='!disabled')
        self.window.frames[6].testNameEntry.delete(0, tk.END)
        self.window.frames[6].durationEntry.configure(state='!disabled')
        self.window.frames[6].durationEntry.delete(0, tk.END)
        self.window.frames[6].saveButton.state(['!disabled'])
        #self.window.frames[5].addQuestionFrame.createNewButton.state(['!disabled'])

        self.window.show_frame(6)