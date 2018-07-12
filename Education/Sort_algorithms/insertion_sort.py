from auxiliary import *


def insertion_sort(arr, verbose=False):
    for sort_len in range(1, len(arr)):
        cur_item = arr[sort_len]
        if verbose:
            print('Cur item:', cur_item)
        insert_index = sort_len
        while insert_index > 0 and cur_item < arr[insert_index - 1]:
            arr[insert_index] = arr[insert_index - 1]
            insert_index -= 1
        arr[insert_index] = cur_item
        if verbose:
            print('Insert ind:', insert_index)
            print('Arr:', arr)
    return arr


if __name__ == '__main__':
    run(insertion_sort, True)
    compare(insertion_sort, 'Insertion Sort')
