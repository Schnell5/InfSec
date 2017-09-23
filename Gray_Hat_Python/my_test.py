import my_debugger
from builtins import int

debugger = my_debugger.debugger()

#debugger.load("C:\\Windows\\System32\\calc.exe")

pid = int(input("Enter the PID of the process to attach to: "))

debugger.attach(pid)

list_threads = debugger.enumerate_threads()

# For each thread in the list we want to grab the
# value of each of the registers

for thread in list_threads:
    
    thread_context = debugger.get_thread_context(thread)
    
    # Now let's output the contents of some of the registers    
    print("[*] Dumping registers for thread ID 0x{0:08x}".format(thread))
    print("[**] EIP: 0x{0:08x}".format(thread_context.Eip))
    print("[**] ESP: 0x{0:08x}".format(thread_context.Esp))
    print("[**] EBP: 0x{0:08x}".format(thread_context.Ebp))
    print("[**] EAX: 0x{0:08x}".format(thread_context.Eax))
    print("[**] EBX: 0x{0:08x}".format(thread_context.Ebx))
    print("[**] ECX: 0x{0:08x}".format(thread_context.Ecx))
    print("[**] EDX: 0x{0:08x}".format(thread_context.Edx))
    print("[*] END DUMP")
    
debugger.detach()




