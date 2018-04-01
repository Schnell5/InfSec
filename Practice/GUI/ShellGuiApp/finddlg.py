from tkinter import *
from ShellGuiApp.formrows import makeFormRow
from find import findlist


def findDialog():
    win = Toplevel()
    win.title('Search criteria')
    var1 = makeFormRow(win, 'Pattern', browse=False)
    var2 = makeFormRow(win, 'Base directory', btn_text='browse...')
    Button(win, text='OK', width=10, command=win.destroy).pack()
    win.grab_set()
    win.focus_set()
    win.wait_window()

    return var1.get(), var2.get()


def runFindDialog():
    pattern, directory = findDialog()
    if pattern != "" and directory != "":
        print('Search pattern:', pattern)
        print('Base directory:', directory)
        print('Search result:')
        for item in findlist(pattern, directory):
            print('=>', item)


if __name__ == '__main__':
    root = Tk()
    Button(root, text='Popup', command=runFindDialog).pack(fill=X)
    Button(root, text='Bye', command=root.quit).pack(fill=X)
    root.mainloop()
