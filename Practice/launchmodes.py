import os
import sys
import time


pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python3'
pypath = sys.executable


def fixWindowsPath(cmdline):
    splitline = cmdline.lstrip().split()
    fixedpath = os.path.normpath(splitline[0])
    return ' '.join([fixedpath] + splitline[1:])


class LaunchMode:
    def __init__(self, label, comand):
        self.what = label
        self.where = comand

    def __call__(self):
        self.announce(self.what)
        self.run(self.where)

    def announce(self, text):
        print(text)

    def run(self, cmdline):
        assert False, 'run must be defined'


class System(LaunchMode):
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.system('{0} {1}'.format(pypath, cmdline))


class Popen(LaunchMode):
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.popen(pypath + ' ' + cmdline)


class Fork(LaunchMode):
    def run(self, cmdline):
        assert hasattr(os, 'fork')
        cmdline = cmdline.split()
        if os.fork() == 0:
            os.execvp(pypath, [pyfile] + cmdline)


class Start(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        cmdline = fixWindowsPath(cmdline)
        os.startfile(cmdline)


class StartArgs(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        os.system('start' + cmdline)


class Spawn(LaunchMode):
    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))


if sys.platform[:3] == 'win':
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork


class QuietPortableLauncher(PortableLauncher):
    def announce(self, text):
        pass


def selftest():
    file = 'echo.py'
    input('Default mode...')
    launcher = PortableLauncher(file, file)
    launcher()

    time.sleep(5)
    input('System mode...')
    System(file, file)()

    if sys.platform[:3] == 'win':
        input('DOS start mode...')
        StartArgs(file, file)()


if __name__ == '__main__':
    selftest()


