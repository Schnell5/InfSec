from tkinter import *
from quitter import Quitter


class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets(options)

    def handlelist(self, event):
        index = self.listbox.curselection()
        label = self.listbox.get(index)
        self.runCommand(label)

    def makeWidgets(self, options):
        sbar = Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH)
        pos = 0
        for label in options:
            list.insert(pos, label)
            pos += 1
        list.bind('<Double-1>', self.handlelist)
        self.listbox = list

    def runCommand(self, selection):
        print('You selected:', selection)


if __name__ == '__main__':
    options = (('Test string - {0}'.format(x)) for x in range(20))
    root = Tk()
    Quitter(root).pack(side=BOTTOM)
    ScrolledList(options, root).pack()
    root.mainloop()
