"""
Compare multiple different sorting functions with each other.
Executes each function in a separate thread and uses the same arrays
in all cases.

Caveat: because of Python's GIL this script gives incorrect results (the returning sort time
for each case is bigger than it really is).
"""

import threading
import queue
from time import time
import copy
from auxiliary import create_array

"""
Import your sort functions below
"""
# Functions to test
from bubble import bubble_sort
from selection_sort import selection_sort
from selection_sort import selection_sort_new
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
    #print('Thread:', threading.current_thread())

    # Without this deepcopy it will be the list of already sorted arrays.
    # We could use my_arr = arrlist[:] but the lists inside arrlist
    # will be the same objects for each thread.
    # >>> lone = [[1, 2, 3], [5, 6, 7], [5, 5, 5]]
    # >>> ltwo = lone[:]
    # >>> lone is ltwo => False
    # >>> lone[1] is ltwo[1] => True (incorrect in our case)
    my_arr = copy.deepcopy(arrlist)

    for i, arr in enumerate(my_arr):
        t0 = time()
        func(arr)
        t1 = time()
        dataqueue.put((name, t1 - t0))


def mult_compare(funclist=[(),], n=[10, 100, 1000, 10000]):
    funclist.append(('Built-In', sorted))                   # Append Built-In sorted func
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
                ('Selec_new', selection_sort_new),
                ('Insertion', insertion_sort)]

    mult_compare(funclist)
