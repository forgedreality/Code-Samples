# Max Min
# https://www.hackerrank.com/challenges/angry-children/problem
def maxMin(k, arr):
    k -= 1
    sorted(arr)
    return min(arr[i + k] - arr[i] for i in range(len(arr) - k))

k = 3
arr = [7, 4, 200, 9, 12, 20, 21, 204, 240]
print(maxMin(k, arr))