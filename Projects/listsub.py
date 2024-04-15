# subtract all elements in array and return largest difference

# test_list = [8, 19, 3, 2, 7]
test_list = [1, 5, 3, 4, 2]
nums = [1, 5, 3, 4, 2]
difference = 2

# iterate over all possible pairs in list and return the absolute value difference between two elements, adding to list res
# res = [abs(a - b) for idx, a in enumerate(test_list) for b in test_list[idx + 1:]]
# Return only those items that match a condition
res = [abs(a - b) for idx, a in enumerate(test_list) for b in test_list[idx + 1:] if abs(a - b) == 2]
c = [abs(a - b) for idx, a in enumerate(nums) for b in nums[idx + 1:] if abs(a - b) == difference]

# get largest difference from list created above
# print(max(res))
print(c)

[__import__("winsound").Beep(x,y) for x,y in [(587, 200), (587, 200), (1174, 400), (880, 600), (830, 400), (783, 400), (698, 400), (587, 200), (698, 200), (783, 200), (523, 200), (523, 200), (1174, 400), (880, 600), (830, 400), (783, 400), (698, 400), (587, 200), (698, 200), (783, 200), (493, 200), (493, 200), (1174, 400), (880, 600), (830, 400), (783, 400), (698, 400), (587, 200), (698, 200), (783, 200), (466, 200), (466, 200), (1174, 400), (880, 600), (830, 400), (783, 400), (698, 400), (587, 200), (698, 200), (783, 200)]]