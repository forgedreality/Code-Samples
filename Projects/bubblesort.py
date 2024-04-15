# bubble sort

def bubblesort(arr):
    swapCount = 0
    for idx,e in enumerate(arr):
        for i in range(len(arr) - 1):
            if i < len(arr) - 1 and arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapCount += 1

    return f'Array is sorted in {swapCount} swaps.\nFirst Element: {arr[0]}\nLast Element: {arr[-1]}\n'


arr = [5, 2, 7, 1, 15, 6, 1, 8]
print(bubblesort(arr), arr)

# arr = [4, 3, 1, 2]
arr = [4, 1, 3, 2]
print(bubblesort(arr), arr)
