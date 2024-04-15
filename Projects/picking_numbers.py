# picking numbers
# find the longest subarray within the given array that has a range of no greater than 1
# i.e., all numbers of the subarray must be within 1 integer of each other.  return the longest subarray.

'''
n=int(input())
l=[int(i) for i in input().split()]
maximum=0
for i in l:
    c=l.count(i)
    d=l.count(i-1)
    c=c+d
    if c > maximum:
        maximum=c
print(maximum)
'''

def pickingNumbers(a):
    return max([a.count(i) + a.count(i - 1) for i in a])

print(pickingNumbers([1, 2, 2, 3, 1, 2]))