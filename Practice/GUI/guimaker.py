import sys
from tkinter import *
from tkinter.messagebox import showinfo


class GuiMaker(Frame):
    menuBar = []
    toolBar = []
    helpButton = True

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.start()
        self.makeMenuBar()
        self.makeToolBar()
        self.makeWidgets()

    def makeMenuBar(self):
        menubar = Frame(self)
        menubar.pack(side=TOP, fill=X)

        for (name, key, items) in self.menuBar:
            mbutton = Menubutton(menubar, text=name, underline=key)
            mbutton.pack(side=LEFT)
            pulldown = Menu(mbutton)
            self.addMenuItems(pulldown, items)
            mbutton.config(menu=pulldown)

        if self.helpButton:
            Button(menubar, text='Help',
                            cursor='gumby',
                            relief=FLAT,
                            command=self.help).pack(side=RIGHT)

    def addMenuItems(self, menu, items):
        for item in items:
            if item == 'separator':
                menu.add_separator({})
            elif isinstance(item, list):
                for num in item:
                    menu.entryconfigure(num, state=DISABLED)
            elif not isinstance(item[2], list):
                menu.add_command(label=item[0], underline=item[1], command=item[2])
            else:
                pullover = Menu(menu)
                self.addMenuItems(pullover, item[2])
                menu.add_cascade(label=item[0], underline=item[1], menu=pullover)

    def makeToolBar(self):
        if self.toolBar:
            toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
            toolbar.pack(side=BOTTOM, fill=X)
            for (name, action, where) in self.toolBar:
                Button(toolbar, text=name, command=action).pack(where)

    def makeWidgets(self):
        name = Label(self,
                     text=self.__class__.__name__,
                     relief=SUNKEN, bg='white',
                     cursor='crosshair')
        name.pack(expand=YES, side=TOP, fill=BOTH)

    def help(self):
        showinfo('Help', 'Sorry, no help for ' + self.__class__.__name__)

    def start(self):
        pass


GuiMakerFrameMenu = GuiMaker


class GuiMakerWindowMenu(GuiMaker):
    def makeMenuBar(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        for (name, key, items) in self.menuBar:
            pulldown = Menu(menubar)
            self.addMenuItems(pulldown, items)
            menubar.add_cascade(label=name, menu=pulldown, underline=key)

        if self.helpButton:
            if sys.platform.startswith('win'):
                menubar.add_command(label='Help', command=self.help)
            else:
                pulldown = Menu(menubar)
                pulldown.add_command(label='About', command=self.help)
                menubar.add_cascade(label='Help', menu=pulldown)


if __name__ == '__main__':
    from guimixin import GuiMixin

    menuBar = [('File', 0, [('Open', 0, lambda:0),
                            ('Quit', 0, sys.exit)]),
               ('Edit', 0, [('Cut', 0, lambda:0),
                            ('Paste', 0, lambda:0)])]
    toolBar = [('Quit', sys.exit, {'side': LEFT})]

    class TestAppFrameMenu(GuiMixin, GuiMakerFrameMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar


    class TestAppWindowMenu(GuiMixin, GuiMakerWindowMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar


    class TestAppWindowBasic(GuiMakerWindowMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar

    root = Tk()
    TestAppFrameMenu(Toplevel())
    TestAppWindowMenu(Toplevel())
    TestAppWindowBasic(root)
    root.mainloop()
