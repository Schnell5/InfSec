import _thread as thread
import queue
import sys

threadQueue = queue.Queue(maxsize=0) # infinite size


# Consumer. Function that works in the main flow and checks Queue object
# This function runs thread handlers from Queue object to get information
def threadChecker(widget, delayMsec=100, perEvent=1):
    for i in range(perEvent):
        try:
            callback, args = threadQueue.get(block=False)
        except queue.Empty:
            break
        else:
            callback(*args)
    widget.after(delayMsec, lambda: threadChecker(widget, delayMsec, perEvent))


# Producer. Function that work in thread flows and fill Queue object with
# thread handlers (onExit, onFail, onProgress)
def threaded(action, args, context, onExit, onFail, onProgress):
    try:
        if not onProgress:
            action(*args)
        else:
            def progress(*smthng):
                threadQueue.put((onProgress, smthng + context))
            action(progress=progress, *args)
    except Exception:
        threadQueue.put((onFail, (sys.exc_info(),) + context))
    else:
        threadQueue.put((onExit, context))


# Start a new thread
def startThread(action, args, context, onExit, onFail, onProgress=None):
    thread.start_new_thread(threaded, (action, args, context, onExit, onFail, onProgress))


if __name__ == '__main__':
    import time
    from tkinter.scrolledtext import ScrolledText

    def onEvent(i):
        myname = 'thread-{0}'.format(i)
        startThread(
            action=threadaction,
            args=(i, 3),
            context=(myname,),
            onExit=threadexit,
            onFail=threadfail,
            onProgress=threadprogress
        )

    # Thread 'action'. Thread will run it
    def threadaction(id, reps, progress):
        for i in range(reps):
            time.sleep(1)
            if progress:
                progress(i)
        if id % 2 == 1:
            raise Exception

    # All handlers below (onExit, onFail, onProgress) will be executed in the main flow where
    # GUI works. Therefore these handlers can safely update widgets of this GUI.
    # Note: sometimes it is possible to update widgets from threads but it can lead to
    # unpredictable results.

    # onExit handler
    def threadexit(myname):
        text.insert('end', '{0}\texit\n'.format(myname))
        text.see('end')

    # onFail handler
    def threadfail(exc_info, myname):
        text.insert('end', '{0}\tfail\t{1}\n'.format(myname, exc_info))
        text.see('end')

    # onProgress handler
    def threadprogress(count, myname):
        text.insert('end', '{0}\tprog\t{1}\n'.format(myname, count))
        text.see('end')
        text.update()

    text = ScrolledText()
    text.pack(expand='yes', fill='both')
    threadChecker(text)
    text.bind('<Button-1>', lambda event: list(map(onEvent, range(6)))) # Create 6 threads
    text.mainloop()
