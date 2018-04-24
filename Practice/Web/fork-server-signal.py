import os
import time
import sys
import signal
from socket import *

myHost = ''
myPort = 55555

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)       # For zombie-processes deleting


def now():
    return time.ctime(time.time())


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
        childPid = os.fork()
        if childPid == 0:
            handleClient(connection)


dispatcher()
