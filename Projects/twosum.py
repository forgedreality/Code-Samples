# TwoSum
def twosum(target, nums):
    out = []
    for i in nums:
        comp = target - i
        if comp in nums:
            out.extend([comp, i])
            return out
    return 'Not found'

print(twosum(23, [4, 17, 6, 12, 5, 9, 2, 1, 48, 19, 27, 8, 7, 10, 15]))
