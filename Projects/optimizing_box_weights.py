# optimizing box weights
#!/bin/python3

#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# UNFINISHED
def dp(arr):
                     # x coordinate, length of arr + 1 (including 0)
                               # height will be our mid-point so that we can cut the time complexity
    width, height = (len(arr), sum(arr)//2)

    # sort the list so we can consider largest values first
    sorted(arr)
    inList = set((arr))
    for row_index, row_value in enumerate(inList):
        for comp in range(height):
            print(comp + row_value)

    output = [[0 for col in range(width)] for row in range(height)]

    for row_index, row in enumerate(output):
        for col_index, col in enumerate(row):
            output[row_index][col_index] = arr[col_index] + row_index

    return output

'''
input list:    [5,3,2,4,1,2]
[
    [0,  1,  2,  3,  4,  5 ],
    [1,  2,  3,  4,  5,  6 ],
    [2,  3,  4,  5,  6,  7 ],
    [3,  4,  5,  6,  7,  8 ],
    [4,  5,  6,  7,  8,  9 ],
    [5,  6,  7,  8,  9,  10],
    [6,  7,  8,  9,  10, 11],
    [7,  8,  9,  10, 11, 12],
    [8,  9,  10, 11, 12, 13]
]
'''


def minHeaviestSet(arr):
    # n = len(arr)
    arr_sum = sum(arr)

    # subset sum problem
    solution_grid = dp(arr)

    return solution_grid

'''
def findMinHeaviest(arr, min_sum, num_needed, found_list):
    if num_needed < 0:
        return []
    
    if num_needed == 0:
        if sum(found_list) > min_sum:
            return [found_list]

        return []

    results = []
    for i in range(len(arr)):
        chosen = arr[i]
        left_arr = arr[0 : i]
        right_arr = arr[i + 1 : 0]
        next_arr = left_arr + right_arr

        temp_results = findMinHeaviest(next_arr, min_sum, num_needed - 1, found_list + [chosen])
        results += temp_results

    return results

'''
def minimalHeaviestSetA(arr):
    '''
    outputA = []
    outputB = arr.copy()
    # sorted(outputB)
    target = math.ceil(sum(arr)/2)

    # sort without using a built in method
    for idx,e in enumerate(outputB):
        for i in range(len(outputB) - 1):
            if i < len(outputB) - 1 and outputB[i] < outputB[i + 1]:
                outputB[i], outputB[i+1] = outputB[i+1], outputB[i]


    results = []
    for i in range(len(arr)):
        chosen = arr[i]
        left_arr = arr[0:i]
        right_arr = arr[i+1:0]
        next_arr = left_arr + right_arr

        temp_results = minimalHeaviestSetA(next_arr)
        results += temp_results
    '''

    # sort without using a built in method
    for idx,e in enumerate(arr):
        for i in range(len(arr) - 1):
            if i < len(arr) - 1 and arr[i] < arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    min_sum = sum(arr) // 2

    for size in range(1, len(arr)):
        results = findMinHeaviest(arr, min_sum, size, [])
        if results:
            return results[0]
            break

    return -1

# print(minimalHeaviestSetA(ar))


# def splitSearch(target, source):
#     if len(source) == 1:
#         r = abs(target - source[0])
#         return r

#     midindex = math.ceil(len(source)/2)

#     if abs(target - source[len(source) - 1]) < abs(target - source[0]):
#         source.reverse()

#     return splitSearch(target, source[:midindex])


# print(minimalHeaviestSetA([5,3,2,4,1,2]))
print(minHeaviestSet([5,3,2,4,1,2]))