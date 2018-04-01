from tkinter import *
from ShellGuiApp.formrows import makeFormRow
from search_all import searcher


def findStrDialog():
    win = Toplevel()
    win.title('Search criteria')
    var1 = makeFormRow(win, 'String', browse=False)
    var2 = makeFormRow(win, 'Base directory', btn_text='browse...')
    Button(win, text='OK', width=10, command=win.destroy).pack()
    win.grab_set()
    win.focus_set()
    win.wait_window()

    return var1.get(), var2.get()


def runFingStrDialog():
    string, directory = findStrDialog()
    if string != "" and directory != "":
        print('String to search:', string)
        print('Base directory:', directory)
        searcher(directory, string)


if __name__ == '__main__':
    root = Tk()
    Button(root, text='Popup', command=runFingStrDialog).pack(fill=X)
    Button(root, text='Bye', command=root.quit).pack(fill=X)
    root.mainloop()