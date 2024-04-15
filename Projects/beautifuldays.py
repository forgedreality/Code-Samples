# Beautiful Days
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def revNum(i):
    return int(str(i)[::-1])

def beautifulDays(i, j, k):
    diff = 0
    days = 0
    for x in range(i, j + 1):
        diff = abs(x - revNum(x))
        days += 1 if diff % k == 0 else 0
    return days

print(beautifulDays(20, 23, 6))