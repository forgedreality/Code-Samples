# Subarray division
# https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem

def birthday(s, d, m):
    sumx = 0
    ways = 0

    for i in range(m):
        sumx += s[i]

    for j in range(len(s) - m + 1):
        if sumx == d:
            ways += 1
        if j + m < len(s):
            sumx = sumx - s[j] + s[j + m]

    return(ways)


print(birthday([1, 2, 1, 3, 2], 3, 2))