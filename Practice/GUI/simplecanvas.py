from tkinter import *


trace = False


class CanvasDraw:
    def __init__(self, parent=None):
        canvas = Canvas(width=700, height=700, bg='beige')
        canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart)
        canvas.bind('<B1-Motion>', self.onGrow)
        canvas.bind('<Double-1>', self.onClear)
        canvas.bind('<ButtonPress-2>', self.onMove)
        self.canvas = canvas
        self.drawn = None
        self.kinds = [canvas.create_oval, canvas.create_rectangle]

    def onStart(self, event):
        self.shape = self.kinds[0]
        self.kinds = self.kinds[1:] + self.kinds[:1]
        self.start = event
        self.drawn = None

    def onGrow(self, event):
        canvas = event.widget
        if self.drawn:
            canvas.delete(self.drawn)
        objectid = self.shape(self.start.x, self.start.y, event.x, event.y)
        if trace:
            print(objectid)
        self.drawn = objectid

    def onMove(self, event):
        print('On move')
        print('Got:', self.drawn)
        if self.drawn:
            if trace:
                print(self.drawn)
            canvas = event.widget
            diffx, diffy = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffx, diffy)
            self.start = event

    def onClear(self, event):
        event.widget.delete('all')


if __name__ == '__main__':
    CanvasDraw()
    mainloop()
