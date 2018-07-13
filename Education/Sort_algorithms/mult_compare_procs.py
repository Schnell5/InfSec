"""
Compare multiple different sorting functions with each other.
Executes each function in a separate processes and uses the same arrays
in all cases.
"""

import multiprocessing as mp
import queue
import copy
from time import time
from auxiliary import create_array

"""
Import your sort functions below
"""
# Functions to test
from bubble import bubble_sort
from selection_sort import selection_sort
from selection_sort import selection_sort_new
from insertion_sort import insertion_sort

dataqueue = mp.Queue()


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
def calculate(name, func, arrlist, dqueue):
    # Without this deepcopy it will be the list of already sorted arrays.
    # We could use my_arr = arrlist[:] but the lists inside arrlist
    # will be the same objects for each process.
    # >>> lone = [[1, 2, 3], [5, 6, 7], [5, 5, 5]]
    # >>> ltwo = lone[:]
    # >>> lone is ltwo => False
    # >>> lone[1] is ltwo[1] => True (incorrect in our case)
    my_arr = copy.deepcopy(arrlist)

    for i, arr in enumerate(my_arr):
        t0 = time()
        func(arr)
        t1 = time()
        dqueue.put((name, t1 - t0))


def mult_compare(funclist=[(),], n=[10, 100, 1000, 10000]):
    funclist.append(('Built-In', sorted))                   # Append Built-In sorted func
    res_list = {name: [] for name, func in funclist}        # List of results
    arrlist = [create_array(i, i) for i in n]               # List of arrays

    # Start calculations in different threads
    for name, func in funclist:
        proc = mp.Process(target=calculate, args=(name, func, arrlist, dataqueue))
        proc.start()

    # Get results until at least one child proccess is alive
    while mp.active_children():
        try:
            name, res = dataqueue.get(block=False)
            res_list[name].append(res)
        except queue.Empty:
            pass

    output(res_list, n)


if __name__ == '__main__':
    funclist = [('Bubble', bubble_sort),
                ('Selection', selection_sort),
                ('Selec_new', selection_sort_new),
                ('Insertion', insertion_sort)]

    mult_compare(funclist)
