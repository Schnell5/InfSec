from auxiliary import *


def selection_sort(arr, verbose=False):
    sort_len = 0
    while sort_len < len(arr):
        min_index = None
        for i, elem in enumerate(arr[sort_len:]):
            if min_index is None or elem < arr[min_index]:
                min_index = i + sort_len
        arr[sort_len], arr[min_index] = arr[min_index], arr[sort_len]
        if verbose:
            print('Swap: {} <-> {}'.format(arr[sort_len], arr[min_index]))
            print('Arr:', arr)
        sort_len += 1
    return arr


def selection_sort_new(arr, verbose=False):
    sort_len = 0
    while sort_len < len(arr):
        min_index = None
        for i in range(sort_len, len(arr)):
            if min_index is None or arr[i] < arr[min_index]:
                min_index = i
        arr[sort_len], arr[min_index] = arr[min_index], arr[sort_len]
        if verbose:
            print('Swap: {} <-> {}'.format(arr[sort_len], arr[min_index]))
            print('Arr:', arr)
        sort_len += 1
    return arr


if __name__ == '__main__':
    run(selection_sort, verbose=True)
    compare(selection_sort, 'Selection Sort')
