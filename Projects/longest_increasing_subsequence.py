# Longest increasing subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

# for longest increasing sequence
def lengthOfLIS(nums: list[int]) -> int:
    count = 1
    rolling_counter = 0
    for i,n in enumerate(nums[1:]):
        if n <= nums[i - 1]: continue

        rolling_counter += 1

        if rolling_counter > count:
            count = rolling_counter
            continue

        count, rolling_counter = 1, 1

    return count


print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([7,7,7,7,7,7,7]))

# for longest subarray
def lengthOfLIS2(nums: list[int]) -> int:
    max_len = 1

    for i,x in enumerate(nums):
        seq = [x]

        for y in nums[i + 1:]:
            if y > seq[-1]:
                seq.append(y)
                print(x, y, seq)
                max_len = max(len(seq), max_len)

    return max_len


print(lengthOfLIS2([10,9,2,5,3,7,101,18]))
print(lengthOfLIS2([7,7,7,7,7,7,7]))
print(lengthOfLIS2([0,1,0,3,2,3]))