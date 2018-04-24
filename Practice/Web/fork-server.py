import os
import time
import sys
from socket import *

myHost = ''
myPort = 55555
activeChildren = []

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)


def now():
    return time.ctime(time.time())


# For zombie-processes deleting
def reapChildren():
    while activeChildren:
        pid, stat = os.waitpid(0, os.WNOHANG)
        if not pid:
            break
        activeChildren.remove(pid)


def handleClient(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data:
            break
        reply = 'Echo => {0} at {1}'.format(data, now())
        connection.send(reply.encode())
    connection.close()
    os._exit(0)


def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print('Server connected by', address, end=' ')
        print('at', now())
        reapChildren()
        childPid = os.fork()
        if childPid == 0:
            handleClient(connection)
        else:
            activeChildren.append(childPid)


dispatcher()
