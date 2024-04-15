# Increment array by 1
# Array given represents a number, with each digit an element in the array.
# Must add one and be able to propagate the carry up to the 0th index
def add_one(input_arr):
    carry = 1
    result = [0] * len(input_arr)

    # Iterate over input array/list in reverse
    # Since enumerate returns a generator, we need to convert it to an iterable using list()
    for i, v in reversed(list(enumerate(input_arr))):
        total = v + carry
        if total == 10:
            carry = 1
        else:
            carry = 0
        result[i] = total % 10

    if carry == 1:
        result = [0] * (len(input_arr) + 1)
        result[0] = 1

    return result

print(add_one([2,3,4,1]))
print(add_one([2,3,4,9]))
print(add_one([1,2,9,9]))
print(add_one([9,9,9]))
print(add_one([0]))
