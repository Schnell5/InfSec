import os
from multiprocessing import Pipe, Process


def sender(pipe):
    pipe.send(['spam'] + [42, 'eggs'])
    pipe.close()


def talker(pipe):
    pipe.send(dict(name='Bob', spam=42))
    reply = pipe.recv()
    print('Talker got:', reply)


if __name__ == '__main__':
    (parentEnd, childEnd) = Pipe()
    Process(target=sender, args=(childEnd,)).start()
    print('Parent got:', parentEnd.recv())
    parentEnd.close()

    (parentEnd, childEnd) = Pipe()
    child = Process(target=talker, args=(childEnd,))
    child.start()
    print('Parent got:', parentEnd.recv())
    parentEnd.send({x * 2 for x in 'spam'})
    child.join()
    print('Parent exit')
