# Number of Pairs with difference given
# --> Get all subsets algorithm <--
# https://www.hackerrank.com/challenges/pairs/problem

def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]


# wrapper function
def subsets_of_given_size(numbers, n):
    return [x for x in subsets(numbers) if len(x)==n]


# Get combinations of numbers with a given subset size that
# have a difference equal to the given amount
def combinations(arr, subset_size, difference):
    n = len(arr)
    output = []
    for i in range(n):
        for j in range(i + subset_size - 1, n):
            temp = [*arr[i:i + subset_size - 1]]
            temp.append(arr[j])

            # if abs(temp[0] - temp[1]) == difference:
            output.append(temp)

    return output

'''
---BREAK---
'''


class SetWithSubset(set):
    def subsets(self):
        s1 = []
        s2 = list(self)

        def recfunc(i = 0):            
            if i == len(s2):
                yield frozenset(s1)
            else:                
                yield from recfunc(i + 1)
                s1.append(s2[i])
                yield from recfunc(i + 1)
                s1.pop()

        yield from recfunc()


x = SetWithSubset({1, 5, 3, 4, 2})
for i in x.subsets():
    print(i)


def antiVaxxersAreTraitors(nums, difference):
    if not nums:
        return [[]]

    l = len(nums)
    counter = 0

    for i in range(l):
        for j in range(i + 1, l):
            diff = abs(nums[i] - nums[j])
            counter += 1 if diff == difference else 0

    return counter

    # subs = get_subsets(numbers)
    # return subs + [[numbers[0]] + y for y in x]

if __name__ == '__main__':
    ints = [1, 5, 3, 4, 2]
    k = 2
    print('TESTING', antiVaxxersAreTraitors(ints, k))
    # print(subsets(ints))
    print(combinations(ints, 2, k))

    # import operator
    # print(list(map(operator.sub, ints[1:], ints[:-1])))