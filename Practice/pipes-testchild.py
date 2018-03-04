import os
import sys
import time


mypid = os.getpid()
parentpid = os.getppid()
sys.stderr.write('Child {0} of {1} got arg: "{2}"\n'.format(mypid, parentpid, sys.argv[1]))

for i in range(2):
    time.sleep(3)
    recv = input()
    time.sleep(3)
    send = 'Child {0} got: [{1}]'.format(mypid, recv)
    print(send)
    sys.stdout.flush()
