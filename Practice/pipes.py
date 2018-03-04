import os
import sys


def spawn(prog, *args):
    stdinfd = sys.stdin.fileno()
    stdoutfd = sys.stdout.fileno()

    parentstdin, childstdout = os.pipe()
    childstdin, parentstdout = os.pipe()
    pid = os.fork()

    if pid:
        os.close(childstdout)
        os.close(childstdin)
        os.dup2(parentstdin, stdinfd)
        os.dup2(parentstdout, stdoutfd)
    else:
        os.close(parentstdout)
        os.close(parentstdin)
        os.dup2(childstdin, stdinfd)
        os.dup2(childstdout, stdoutfd)
        args = (prog,) + args
        os.execvp(prog, args)
        assert False, 'execvp failed!'


if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python3', 'pipes-testchild.py', 'spam')
    print('Hello 1 from parent', mypid)
    sys.stdout.flush()
    reply = input()
    sys.stderr.write('Parent got: {0}\n'.format(reply))
    print('Hello 2 from parent', mypid)
    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('Parent got: {0}\n'.format(reply[:-1]))
