# Array Manipulation
# https://www.hackerrank.com/challenges/crush/problem
def arrayManipulation(n, queries):
    outList = [0]*(n+1)

    # Iterate over input operations
    for q in queries:
        k = q[2]
        outList[q[0]-1] += k
        outList[q[1]] -= k

    sumVal = 0
    maxVal = 0

    for o in outList:
        sumVal += o
        maxVal = max(maxVal, sumVal)
        # if maxVal + o > maxVal:
        #     maxVal = maxVal+o

    return maxVal

# print(arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
print(arrayManipulation(10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]))
print(arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))

