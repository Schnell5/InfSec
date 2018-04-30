import os
import sys
import time
import threading
from socket import *

blksz = 1024
defhost = 'localhost'
defport = 55555

helptext = """
Usage...
server => getfile -mode server [-host hhh|localhost] [-port nnn]
client => getfile [-mode client] -file fff [-host hhh|localhost] [-port nnn] 
"""


def now():
    return time.ctime(time.time())


def parsecommandline():
    dict = {}
    args = sys.argv[1:]
    while len(args) >= 2:
        dict[args[0]] = args[1]
        args = args[2:]
    return dict


def client(host, port, filename):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send((filename + '\n').encode())
    dropdir = os.path.split(filename)[1]    # Get filename (to place in current dir)
    file = open(dropdir, 'wb')
    while True:
        data = sock.recv(blksz)
        if not data:
            break
        file.write(data)
    sock.close()
    file.close()
    print('Client got {0} at {1}'.format(filename, now()))


def serverthread(clientsock):
    sockfile = clientsock.makefile('r')
    filename = sockfile.readline()[:-1]     # Do not include '\n'
    try:
        file = open(filename, 'rb')
        while True:
            bytes = file.read(blksz)
            if not bytes:
                break
            sent = clientsock.send(bytes)
            assert sent == len(bytes)
    except Exception:
        print('Error downloading file on server:', filename)
    clientsock.close()


def server(host, port):
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind((host, port))
    serversock.listen(5)
    while True:
        clientsock, clientaddr = serversock.accept()
        print('Server connected by {0} at {1}'.format(clientaddr, now()))
        threading.Thread(target=serverthread, args=(clientsock,)).start()


def main(args):
    host = args.get('-host', defhost)
    port = int(args.get('-port', defport))
    if args.get('-mode') == 'server':
        if host == 'localhost':
            host = ''
        server(host, port)
    elif args.get('-file'):
        client(host, port, args['-file'])
    else:
        print(helptext)


if __name__ == '__main__':
    args = parsecommandline()
    main(args)
