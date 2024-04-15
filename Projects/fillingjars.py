# Filling Jars
# https://www.hackerrank.com/challenges/filling-jars/problem

def solve(n, operations):
    sumtotal = 0
    for x in operations:
        sumtotal = sumtotal + (x[1] - x[0] + 1) * x[2]
    # This is too time-complex:
    # o = [0] * n
    # for x in operations:
    #     start = x[0] - 1
    #     end = x[1]
    #     replace = range(start, end)
    #     for i in [*replace]:
    #         o[i] += x[2]
    #         i += 1

    return int(sumtotal/n)

print(solve(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))