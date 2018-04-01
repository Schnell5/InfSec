from ShellGuiApp.shellgui import *
from ShellGuiApp.finddlg import runFindDialog
from ShellGuiApp.searchalldlg import runFingStrDialog
from canvasDrawAnim_after import CanvasAnimAfter


class UtilsPack(ListMenuGui):
    def __init__(self):
        self.myMenu = [('find', lambda: self.redirectToGui(runFindDialog)),
                       ('canvasDraw', lambda: CanvasAnimAfter(Toplevel())),
                       ('search_string', lambda: self.redirectToGui(runFingStrDialog))]
        ListMenuGui.__init__(self)

    def forToolBar(self, label):
        return label in {'find', 'search_string'}

    def redirectToGui(self, func, *args, **kwargs):
        import sys
        saveStdout = sys.stdout
        sys.stdout = GuiOutput(self.textfield)
        sys.stderr = sys.stdout
        result = func(*args, **kwargs)
        sys.stdout = saveStdout
        return result


if __name__ == '__main__':
    UtilsPack().mainloop()
