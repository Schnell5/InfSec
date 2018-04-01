import threading
import queue
import time
from tkinter.scrolledtext import ScrolledText


class ThreadGui(ScrolledText):
    threadsPerClick = 4

    def __init__(self, parent=None):
        ScrolledText.__init__(self, parent)
        self.pack()
        self.dataQueue = queue.Queue()
        self.bind('<Button-1>', self.makethreads)
        self.consumer()

    def producer(self, id):
        for i in range(5):
            time.sleep(2)
            self.dataQueue.put('[producer id={0}, count={1}]'.format(id, i))

    def consumer(self):
        try:
            data = self.dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            self.insert('end', 'consumer got => {0}\n'.format(data))
            self.see('end')
        self.after(100, self.consumer)

    def makethreads(self, event):
        for i in range(self.threadsPerClick):
            threading.Thread(target=self.producer, args=(i,)).start()


if __name__ == '__main__':
    root = ThreadGui()
    root.mainloop()
