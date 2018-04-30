from formmaker import Form
from tkinter import Tk, mainloop
from tkinter.messagebox import showinfo
import getfile
import os


class GetFileForm(Form):
    def __init__(self, oneshot=False):
        root = Tk()
        root.title('GetFile')
        labels = ['Server Name', 'Port Number', 'File Name', 'Dir to save']
        Form.__init__(self, labels, root)
        self.oneshot = oneshot

    def onSubmit(self):
        Form.onSubmit(self)
        localdir = self.content['Dir to save'].get()
        portnum = self.content['Port Number'].get()
        servername = self.content['Server Name'].get()
        filename = self.content['File Name'].get()
        if localdir:
            os.chdir(localdir)
        portnum = int(portnum)
        getfile.client(servername, portnum, filename)
        showinfo('GetFile', 'Download complete')
        if self.oneshot:
            Tk().quit()


if __name__ == '__main__':
    GetFileForm()
    mainloop()
