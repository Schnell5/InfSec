"""
Module with auxiliary functions to simplify common operations:
- array creation
- output formatting
- comparison
"""
from random import randint


def create_array(length=10, maxint=50):
    new_array = [randint(0, maxint) for _ in range(length)]
    return new_array


def run(test=lambda x, y: 0, verbose=False):
    print('-' * 30)
    orig = create_array()
    print('Orig:', orig)

    sort = test(orig, verbose)
    print('Sorted:', sort)
    print('-' * 30)


def compare(test_func=lambda x: None, name='Test', n=[10, 100, 1000, 10000]):
    from time import time
    res_test = []
    res_py = []
    for length in n:
        arr = create_array(length, length)

        t0 = time()
        s1 = test_func(arr)
        t1 = time()
        res_test.append(t1 - t0)

        t0 = time()
        s2 = sorted(arr)
        t1 = time()
        res_py.append(t1 - t0)

    print('{0:<8}{1:<10}{2:<10}'.format('n', 'Built-In', name))
    print('-' * 30)
    for i, cur_n in enumerate(n):
        print('{0:<8}{1:<10.5f}{2:<10.5f}'.format(cur_n, res_py[i], res_test[i]))
