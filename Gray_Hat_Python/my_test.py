import my_debugger
from builtins import int

debugger = my_debugger.debugger()

#debugger.load("C:\\Windows\\System32\\calc.exe")

pid = int(input("Enter the PID of the process to attach to: "))

debugger.attach(pid)

debugger.detach()




