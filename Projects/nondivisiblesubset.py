# Non-Divisible Subset
# https://www.hackerrank.com/challenges/non-divisible-subset/problem

def nonDivisibleSubset(k, s):
    d = {x:[] for x in range(k)}

    for i in range(len(s)):
        d[s[i]%k].append(s[i])

    count = 0

    if len(d[0]) > 0:
        count = 1

    S = set([(x, k - x) for x in range(1, k//2+1)])

    for i, j in S:
        if i != j:
            count += len(d[i]) if len(d[i]) > len(d[j]) else len(d[j])

        else:
            if len(d[i]) > 0:
                count += 1

    return count

arr = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
print(nonDivisibleSubset(7, arr))