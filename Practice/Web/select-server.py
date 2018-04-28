import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from select import select

myHost = ''
myPort = 55555
if len(sys.argv) == 3:
    myHost, myPort = sys.argv[1:]
numPortSocks = 2


def now():
    return time.ctime(time.time())


# Create main sockets to receive new client's connections
mainsocks, readsocks, writesocks = [], [], []


for i in range(numPortSocks):
    portsock = socket(AF_INET, SOCK_STREAM)
    portsock.bind((myHost, myPort))
    portsock.listen(5)
    mainsocks.append(portsock)
    readsocks.append(portsock)
    myPort += 1

# Listen and multiplex client's connections
print('select-server loop starting')
while True:
    readables, writables, exceptions = select(readsocks, writesocks, [])
    for sockobj in readables:
        if sockobj in mainsocks:
            # main sock object: accept new client connection
            newsock, address = sockobj.accept()         # non-blocking call
            print('Connect:', address, id(newsock))
            readsocks.append(newsock)
        else:
            # client sock object: read the next line
            data = sockobj.recv(1024)                   # non-blocking call
            print('\tgot', data, 'on', id(sockobj))
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                reply = 'Echo => {0} at {1}'.format(data, now())
                sockobj.send(reply.encode())            # can block
