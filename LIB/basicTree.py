import tkinter as tk
from tkinter import ttk

class MyTree(ttk.Treeview):

    def __init__(self, parent_frame, column_names,r,c):
        ttk.Treeview.__init__(self)
        self.r = r
        self.c = c
        self.style = ttk.Style()
        self.style.configure('Treeview', rowheight=35)
        self.id = 0
        self.iid = 0
        self.parent_frame = parent_frame
        self.column_names = column_names
        self.scrollbar = ttk.Scrollbar(self.parent_frame,orient="vertical")
        self.Tree = ttk.Treeview(self.parent_frame,height = 5,yscrollcommand=self.scrollbar.set,columns = self.column_names)
        for i in range(0, len(self.column_names)+1):
            self.Tree.column('#' + str(i), stretch=tk.FALSE, minwidth=75, width=100)
        self.scrollbar.configure(command=self.Tree.yview)
        self.scrollbar.grid(row = self.r , column = 9, sticky=tk.NS)
        self.Tree.bind('<ButtonRelease-1>',self.selectedItem)
        for name in self.column_names:
            self.Tree.heading(name, text =name)


        self.Tree.grid(row = self.r, column = self.c, padx=5, pady=5,sticky="w", columnspan=8)


    def populateTree(self, records):
        rec_num = 1
        for r in records:
            vals = []
            for i in range(len(r)):
                vals.append(r[i])
            self.Tree.insert("", "end", text=str('Record #' + str(rec_num)), values=(vals))
            rec_num+=1


    def selectedItem(self, evt):
        currentItem = self.Tree.focus()
        rowData = self.Tree.item(currentItem, 'values')


    def clearTree(self):
        self.Tree.delete(*self.Tree.get_children())

    def clearSelected(self):
        selected_item = self.Tree.selection()[0]  ## get selected item
        self.Tree.delete(selected_item)
        return selected_item