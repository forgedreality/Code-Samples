# Utopian Tree
# In Spring, it doubles in height
# In summer, its height increases by 1
# Odds = spring, evens = summer ?
# Starts at a height of 1 meter

def utopianTree(n):
    result = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            result += 1
        else:
            result *= 2

    return result