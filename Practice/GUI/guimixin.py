from tkinter import *
from scrolledtext import ScrolledText
from tkinter.messagebox import *
from tkinter.filedialog import *
from launchmodes import PortableLauncher, System


class GuiMixin:
    def infobox(self, title, text, *args):
        return showinfo(title, text)

    def errorbox(self, text):
        showerror('Error!', text)

    def question(self, title, text, *args):
        return askyesno(title, text)

    def notdone(self):
        showerror('Not implemented', 'Option not available')

    def quit(self):
        ans = self.question('Verify quit', 'Are you sure you want to quit?')
        if ans:
            Frame.quit(self)

    def help(self):
        self.infobox('Help', 'See figure 1')

    def selectOpenFile(self, file="", direct="."):
        return askopenfilename(initialfile=file, initialdir=direct)

    def selectSaveFile(self, file="", direct="."):
        return asksaveasfilename(initialfile=file, initialdir=direct)

    def clone(self, args=()):
        new = Toplevel()
        myclass = self.__class__
        myclass(new, *args)

    def spawn(self, pycmdline, wait=False):
        if not wait:
            PortableLauncher(pycmdline, pycmdline)()
        else:
            System(pycmdline, pycmdline)()

    def browser(self, filename):
        new = Toplevel()
        view = ScrolledText(new, file=filename)
        view.text.config(height=30, width=85)
        view.text.config(font=('courier', 14, 'normal'))
        new.title("Text viewer")
        new.iconname("Browser")


if __name__ == '__main__':
    class TestMixin(GuiMixin, Frame):
        def __init__(self, parent=None):
            Frame.__init__(self, parent)
            self.pack()
            Button(self, text='quit', command=self.quit).pack(fill=X)
            Button(self, text='help', command=self.help).pack(fill=X)
            Button(self, text='clone', command=self.clone).pack(fill=X)
            Button(self, text='spawn', command=self.other).pack(fill=X)

        def other(self):
            self.spawn('guimixin.py')

    TestMixin().mainloop()
