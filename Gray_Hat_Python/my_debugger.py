from my_debugger_defines import *
from ctypes import windll
from _ctypes import sizeof, byref
from _winapi import PROCESS_ALL_ACCESS
from builtins import int
from distutils.log import debug

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = False
    
    def load(self, path_to_exe):
        
        # dwCreation flag determines how to create the process
        # set creation_flags = CREATE_NEW_CONSOLE if you want
        # to see the calculator GUI
        creation_flags = DEBUG_PROCESS
        #creation_flags = CREATE_NEW_CONSOLE
        
        # instantiate the structs
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()
        
        # The following two options allow the started process
        # to be shown as a separate window. This also illustrates
        # how different settings in the STARTUPINFO struct can affect
        # the debuggee.
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        
        # We then initialize the cb variable in the STARTUPINFO struct
        # which is just the size of the struct itself
        startupinfo.cb = sizeof(startupinfo)
        
        if kernel32.CreateProcessW(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)):
            
            print("[*] We have successfully launched the process!")
            print("[*] PID {name}".format(name = process_information.dwProcessId))
            
            # Obtain a valid handle to the newly created process and store it for future access
            self.h_process = self.open_process(process_information.dwProcessId)
            #self.attach(process_information.dwProcessId)
            
        else:
            print("[*] Error 0x{0:08x}".format(kernel32.GetLastError()))
            
    def open_process(self, pid):
        
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        return h_process
    
    def open_thread(self, thread_id):
        
        h_thread = kernel32.OpenThread(THREAD_ALL_ACCESS, None, thread_id)
        
        if h_thread is not None:
            return h_thread
        
        else:
            print("[!] Could not obtain a valid thread handler.")
            return False
        
    def enumerate_threads(self):
        
        thread_entry = THREADENTRY32()
        thread_list = []
        snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, self.pid)
        
        if snapshot is not None:
            # You have to set the size of the struct or the call will fail
            thread_entry.dwSize = sizeof(thread_entry)
            success = kernel32.Thread32First(snapshot, byref(thread_entry))
            
            while success:
                #print("self.pid = ", self.pid)
                #print("thread_entry.th32OwnerProcessID = ", thread_entry.th32OwnerProcessID)
                if thread_entry.th32OwnerProcessID == self.pid:
                    thread_list.append(thread_entry.th32ThreadID)
                    print("thread_lits_new", thread_list)
                    success = kernel32.Thread32Next(snapshot, byref(thread_entry))
            
            kernel32.CloseHandle(snapshot)
            print(thread_list)
            return thread_list
        else:
            print("[!] Could not get the snapshot.")
            return False
        
    def get_thread_context(self, thread_id = None, h_thread = None):
        
        context = CONTEXT()
        context.ContextFlags = CONTEXT_FULL | CONTEXT_DEBUG_REGISTERS
        
        # Obtain a handle to the thread
        if not h_thread:
            self.open_thread(thread_id)
            
        if kernel32.GetThreadContext(h_thread, byref(context)):
            kernel32.CloseHandle(h_thread)
            return context
        else:
            print("[!] Could not get the context of the thread.")
            return False
        
    def attach(self, pid):
        
        self.h_process = self.open_process(pid)
        
        # We attempt to attach to the process if this fails we exit the call
        
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)
            print("[*] Successfully attached to the process.")
            
        else:
            print("[*] Unable to attach to the process.")
            
        
        #while self.debugger_active == True:
        self.get_debug_event()
    
    def get_debug_event(self):
        
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE
        
        if kernel32.WaitForDebugEvent(byref(debug_event), INFINITE):
            
            #input("Press a key to continue...")
            #self.debugger_active = False
            kernel32.ContinueDebugEvent(debug_event.dwProcessId, debug_event.dwThreadId, continue_status)
            print(debug_event.dwProcessId, debug_event.dwThreadId, continue_status)
            
    def detach(self):
        
        if kernel32.DebugActiveProcessStop(self.pid):
            print("[*] Finished debugging. Exiting...")
            return True
        else:
            print("[!] There was an error")
            return False
        
