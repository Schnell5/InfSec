import time
from tkinter.scrolledtext import ScrolledText
from threadtools import threadChecker, startThread


class MyGUI:
    def __init__(self, reps=3):
        self.reps = reps
        self.text = ScrolledText()
        self.text.pack(expand='yes', fill='both')
        threadChecker(self.text, perEvent=4)
        self.text.bind('<Button-1>', lambda event: list(map(self.onEvent, range(6))))

    def onEvent(self, i):
        myname = 'thread-{0}'.format(i)
        startThread(
            action=self.threadaction,
            args=(i, ),
            context=(myname,),
            onExit=self.threadexit,
            onFail=self.threadfail,
            onProgress=self.threadprogress
        )

    def threadaction(self, id, progress):
        for i in range(self.reps):        # We can use data from object itself
            time.sleep(1)
            if progress:
                progress(i)
        if id % 2 == 1:
            raise Exception

    def threadexit(self, myname):
        self.text.insert('end', '{0}\texit\n'.format(myname))
        self.text.see('end')

    def threadfail(self, exc_info, myname):
        self.text.insert('end', '{0}\tfail\t{1}\n'.format(myname, exc_info))
        self.text.see('end')

    def threadprogress(self, count, myname):
        self.text.insert('end', '{0}\tprog\t{1}\n'.format(myname, count))
        self.text.see('end')
        self.text.update()


if __name__ == '__main__':
    MyGUI().text.mainloop()
