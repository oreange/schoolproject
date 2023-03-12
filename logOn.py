import tkinter as tk
from tkinter import ttk

class LogOn(ttk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        packOption ={'ipadx':2,'ipady':2,'padx':5, 'pady':5}
        self.usernameLabel = ttk.Label(self, text = "Username: ")
        self.usernameLabel.pack(**packOption)
        self.usernameEntry = ttk.Entry(self)
        self.usernameEntry.pack(**packOption)
        self.passwordLabel=ttk.Label(self, text = "Password: ")
        self.passwordLabel.pack(**packOption)
        self.passwordEntry=ttk.Entry(self, show="*")
        self.passwordEntry.pack(**packOption)
        self.logButton = ttk.Button(self, text="Log On", command = lambda:self.log())
        self.logButton.pack(anchor=tk.S, **packOption)
        self.grid(row=0, column=0, sticky=tk.NSEW)

    def log(self):
        if self.passwordEntry.get()=="admin":
            self.window.show_frame(0)
        else:
            self.window.show_student_frame(0)


if __name__ =="__main__":
    win = tk.Tk()
    log = LogOn(win)
    win.mainloop()