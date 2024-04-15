'''Implement quick sort in Python.
Input a list.
Output a sorted list.'''
def partition(array, low, high):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = array[high], low

    for i in range(low, high):
        if array[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            array[i], array[ptr] = array[ptr], array[i]
            ptr += 1

    # Finally swapping the last element with the pointer indexed number
    array[ptr], array[high] = array[high], array[ptr]
    return ptr


def quicksort(array, low=None, high=None):
    if low == None:
        low = 0

    if high == None:
        high = len(array) - 1

    if low < high:
        # find pivot element
        # smaller are on the left
        # larger are on the right
        pi = partition(array, low, high)

        # recursive call to left of pivot
        quicksort(array, low, pi - 1)
        # recursive call to right of pivot
        quicksort(array, pi + 1, high)

    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
