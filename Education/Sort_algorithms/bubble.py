from auxiliary import *


def bubble_sort(arr, verbose=False):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                if verbose:
                    print('Swap: {} <-> {}'.format(arr[i-1], arr[i]))
                    print('Array:', arr)
                swapped = True
    return arr


if __name__ == '__main__':
    run(bubble_sort, verbose=True)
    compare(bubble_sort, 'Bubble Sort')
