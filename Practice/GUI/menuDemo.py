from tkinter import *
from tkinter.messagebox import *
from PIL.ImageTk import PhotoImage


class NewMenuDemo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=YES)
        self.createWidgets()
        self.master.title('Toolbars and Menus')
        self.master.iconname('tkpython')

    def createWidgets(self):
        self.makeToolBar()
        self.makeMenuBar()
        lab = Label(self, text='Toolbar and Menu demo')
        lab.config(relief=SUNKEN, width=40, height=10, bg='white')
        lab.pack(fill=BOTH, expand=YES)

    def makeToolBar(self):
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(fill=X, side=BOTTOM, expand=YES)
        Button(toolbar, text='Hello', command=self.greeting).pack(side=LEFT)
        Button(toolbar, text='Quit', command=self.quiter).pack(side=RIGHT)

    def makeMenuBar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.fileMenu()
        self.editMenu()
        self.imageMenu()

    def fileMenu(self):
        pulldown = Menu(self.menubar, tearoff=False)
        pulldown.add_command(label='Open...', command=self.notdone)
        pulldown.add_command(label='Quit', command=self.quiter)
        self.menubar.add_cascade(label='File', menu=pulldown, underline=0)

    def editMenu(self):
        pulldown = Menu(self.menubar, tearoff=False)
        pulldown.add_command(label='Paste', command=self.notdone)
        pulldown.add_command(label='Spam', command=self.greeting)
        self.menubar.add_cascade(label='Edit', menu=pulldown, underline=0)

    def imageMenu(self):
        photodir = '/Users/ekantysev/Desktop/Programming/PP4E-Examples-1.4/Examples/PP4E/Gui/PIL/images'
        photofiles = ('PythonPoweredAnim.gif', 'python_conf_ora.gif', 'lpython_sm_ad.gif')
        pulldown = Menu(self.menubar)
        self.photoobjs = []
        for file in photofiles:
            img = PhotoImage(file=(photodir + '/' + file))
            pulldown.add_command(image=img, command=self.notdone)
            self.photoobjs.append(img)
        self.menubar.add_cascade(label='Image', menu=pulldown, underline=0)

    def greeting(self):
        showinfo('greeting', 'Greetings')

    def notdone(self):
        showerror('Not implemented', 'Not yet available')

    def quiter(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            Frame.quit(self)


if __name__ == '__main__':
    NewMenuDemo().mainloop()
