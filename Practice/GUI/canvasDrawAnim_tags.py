from tkinter import *
from simplecanvas import CanvasDraw
import time


class CanvasAnim(CanvasDraw):
    def __init__(self, parent=None):
        CanvasDraw.__init__(self, parent)
        self.canvas.create_text(110, 10, text='Press o and/or r to move shapes')
        self.canvas.master.bind('<KeyPress-o>', self.onMoveOvals)
        self.canvas.master.bind('<KeyPress-r>', self.onMoveRectangles)
        self.kinds = self.create_oval_tagged, self.create_rectangle_tagged

    def create_oval_tagged(self, x1, y1, x2, y2):
        objectid = self.canvas.create_oval(x1, y1, x2, y2)
        self.canvas.itemconfig(objectid, tag='ovals', fill='blue')
        return objectid

    def create_rectangle_tagged(self, x1, y1, x2, y2):
        objectid = self.canvas.create_rectangle(x1, y1, x2, y2)
        self.canvas.itemconfig(objectid, tag='rectangles', fill='red')
        return objectid

    def onMoveOvals(self, event):
        print('Moving ovals')
        self.moveInSquares(tag='ovals')

    def onMoveRectangles(self, event):
        print('Moving rectangles')
        self.moveInSquares(tag='rectangles')

    def moveInSquares(self, tag):
        for i in range(5):
            for (diffx, diffy) in [(+20, 0), (0, +20), (-20, 0), (0, -20)]:
                self.canvas.move(tag, diffx, diffy)
                self.canvas.update()
                time.sleep(0.25)


if __name__ == '__main__':
    CanvasAnim()
    mainloop()
