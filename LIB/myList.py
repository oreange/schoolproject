import tkinter as tk

class ListWidget(tk.Listbox):

    def __init__(self, parent, r, c):
        super().__init__()
        self.parent = parent
        self.r = r
        self.c = c

        self.list = tk.Listbox(self.parent, width=90, height=10)
        self.list.bind('<<ListboxSelect>>', self.getSlected)
        self.list.grid(row=self.r, column=self.c, padx=5, pady=5, columnspan=5)
        self.scrollbar = tk.Scrollbar(self.parent, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.list.yview)
        self.scrollbar.grid(row=self.r, column=6, sticky=tk.NS)
        self.list.config(yscrollcommand=self.scrollbar.set)

    def fillList(self, data):
        # clear
        self.list.delete(0, tk.END)
        for item in data:
            # remove empty space from the tuple
            string = ''
            for word in item:
                string += f"{str(word)},"
            self.list.insert(tk.END, string)

    def getSlected(self, evt):
        item = self.list.get(tk.ACTIVE)
        return item





if __name__ == "__main__":
    pass
