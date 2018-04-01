from tkinter import *
from guimaker import *
from guimixin import GuiMixin
from scrolledtext import ScrolledText


class GuiOutput:
    def __init__(self, dest):
        self.dest = dest

    def write(self, text):
        self.dest.insert(END, str(text))
        self.dest.update()


class ShellGui(GuiMixin, GuiMakerWindowMenu):
    def start(self):
        self.setMenuBar()
        self.setToolBar()
        self.master.title("Shell Tools")
        self.master.iconname("Shell Tools")

    def forToolBar(self, label):
        return True

    def handlelist(self, event):
        label = self.listbox.get(ACTIVE)
        self.runCommand(label)

    def setMenuBar(self):
        toolEntries = []
        self.menuBar = [('File', 0, [('Quit', -1, self.quit)]),
                        ('Tools', 0, toolEntries)]
        for (label, action) in self.fetchCommands():
            toolEntries.append((label, -1, action))

    def setToolBar(self):
        self.toolBar = []
        for (label, action) in self.fetchCommands():
            if self.forToolBar(label):
                self.toolBar.append((label, action, dict(side=LEFT)))
        self.toolBar.append(('Quit', self.quit, dict(side=RIGHT)))
        self.toolBar.append(('Clear', lambda: self.textfield.delete('1.0', END), dict(side=RIGHT)))

    def makeList(self):
        class ListScroll(Frame):
            def __init__(self, parent=None):
                Frame.__init__(self, parent)
                self.makelist()

            def makelist(self):
                listbox = Listbox(self)
                sbar = Scrollbar(self)
                listbox.config(yscrollcommand=sbar.set)
                sbar.config(command=listbox.yview)
                sbar.pack(side=RIGHT, fill=Y)
                listbox.pack(side=LEFT, fill=BOTH, expand=YES)
                self.listbox = listbox

        listscroll = ListScroll(self)
        return listscroll

    def makeWidgets(self):
        listscroll = self.makeList()
        textfield = ScrolledText(self)
        listscroll.pack(side=LEFT, expand=YES, fill=BOTH)
        textfield.pack(side=RIGHT, expand=YES, fill=BOTH)
        for (label, action) in self.fetchCommands():
            listscroll.listbox.insert(END, label)
        listscroll.listbox.bind('<Double-1>', self.handlelist)
        self.listbox = listscroll.listbox
        self.textfield = textfield.text


class ListMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu

    def runCommand(self, cmd):
        for (label, action) in self.myMenu:
            if label == cmd:
                action()
