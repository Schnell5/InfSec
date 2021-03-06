from tkinter import *
from tkinter.messagebox import askokcancel


class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit, padx=50)
        widget.pack(side=LEFT, fill=BOTH, expand=YES)

    def quit(self):
        ans = askokcancel('Verify exit', 'Really quit?')
        if ans:
            Frame.quit(self)


if __name__ == '__main__':
    Quitter().mainloop()
