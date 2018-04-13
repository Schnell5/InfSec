from tkinter import *
from tkinter.filedialog import askdirectory


def makeFormRow(parent, label, width=15, browse=True, btn_text="", extend=False):
    var = StringVar()
    row = Frame(parent)
    label = Label(row, text=label + '?', width=width)
    ent = Entry(row, textvariable=var)
    row.pack(fill=X)
    label.pack(side=LEFT)
    ent.pack(side=LEFT, expand=YES, fill=X)
    if browse:
        btn = Button(row, text=btn_text)
        btn.pack(side=RIGHT)
        btn.config(command=lambda: var.set(askdirectory() or var.get()))
    return var
