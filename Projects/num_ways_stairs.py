# number of ways you can climb to the top of a staircase of n steps
# optional parameter says how many steps you are allowed to climb at once
#  - default [1,2] means you can go 1 step or 2 steps.

def num_ways_to_climb_stairs(n, allowed_steps=[1, 2]):
    # if only considering 1 or 2 steps at a time, we don't need to create a whole list,
    # we can just consider two positions at once.
    if allowed_steps == [1, 2]:
        one, two = 1, 1

        for _ in range(n - 1):
            # add our previous two results, and shift window back by setting two to one's previous value
            one, two = one + two, one

        return one

    # while this method also works for 1 or 2 steps, different numbers of steps makes the sliding window technique
    # more difficult, so we store the entire array of results.
    else:
        if n == 0:
            return 1

        nums = [0] * (n+1)
        nums[0] = 1

        for i in range(1, n+1):
            total = 0
            for j in allowed_steps:
                if i - j >= 0:
                    total += nums[i - j]
            nums[i] = total

        return nums[n]

# def num_ways_to_climb_stairs(n, allowed_steps=[1, 2]):
#     one, two = 1, 1

#     for s in range(n - 1):
#         # add our previous two results, and shift window back by setting two to one's previous value
#         one, two = one + two, one

#     return one

'''
# timeit example
import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

test = wrapper(num_ways_to_climb_stairs, 6)

print(timeit.timeit(test, number=1000))
'''

print(num_ways_to_climb_stairs(6))
print(num_ways_to_climb_stairs(6, [1,3,5]))
print(num_ways_to_climb_stairs(14, [1,2,3]))
print(num_ways_to_climb_stairs(14))
print(num_ways_to_climb_stairs(13, [1,2,3]))
