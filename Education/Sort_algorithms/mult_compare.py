"""
Compare multiple different sorting functions with each other.
Executes each function in a separate thread and uses the same arrays
in all cases.
"""

import threading
import queue
from time import time
from auxiliary import create_array

"""
Import your sort functions below
"""
# Function to test
from bubble import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

dataqueue = queue.Queue(maxsize=0)


# Print output table
def output(res_list, n):
    func_names = sorted(res_list)
    func_names.remove('Built-In')
    row = '{:<8}{:<10}' + '{:<10}' * len(func_names)
    print('-' * (15 * (len(func_names) + 1)))
    print(row.format('n', 'Built-In', *func_names))     # Header
    print('-' * (15 * (len(func_names) + 1)))
    for i, cur_n in enumerate(n):
        row = '{:<8}{:<10.5f}'.format(cur_n, res_list['Built-In'][i])
        for elem in func_names:
            row += '{:<10.5f}'.format(res_list[elem][i])
        print(row)


# Calculate result in threads
def calculate(name, func, arrlist):
    # print('Thread:', threading.current_thread())
    for i, arr in enumerate(arrlist):
        t0 = time()
        func(arr)
        t1 = time()
        dataqueue.put((name, t1 - t0))


def mult_compare(funclist=[(),], n=[10, 100, 1000, 10000]):
    funclist.append(('Built-In', sorted))                   # Append Built-In sorting func
    res_list = {name: [] for name, func in funclist}        # List of results
    threads = []                                            # List of active threads
    arrlist = [create_array(i, i) for i in n]               # List of arrays

    # Start calculations in different threads
    for name, func in funclist:
        thread = threading.Thread(target=calculate, args=(name, func, arrlist))
        thread.start()
        threads.append(thread)

    # Get results until at least one thread is alive
    while threads:
        try:
            name, res = dataqueue.get(block=False)
            res_list[name].append(res)
            # print(res_list)
            # Check threads
            threads = [thr for thr in threads if thr.is_alive()]
            # print(threads)
        except queue.Empty:
            pass

    output(res_list, n)


if __name__ == '__main__':
    funclist = [('Bubble', bubble_sort),
                ('Selection', selection_sort),
                ('Insertion', insertion_sort)]

    mult_compare(funclist)
