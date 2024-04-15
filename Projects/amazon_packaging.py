# Amazon packaging automation
def groupPackages(arr):
    if len(arr) == 1: return 1

    arr.sort()
    arr[0] = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            arr[i] = arr[i - 1] + 1
    print(arr)

    return arr[-1]


if __name__ == '__main__':
    input_array = [5,3,2,2,6]
    print(groupPackages(input_array))