import threading
import time
from socket import *

myHost = ''
myPort = 55555

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)


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


def dispatcher():
    while True:
        connection, addr = sockobj.accept()
        print('Server connected by', addr, end=' ')
        print('at', now())
        threading.Thread(target=handleClient, args=(connection,)).start()


dispatcher()
