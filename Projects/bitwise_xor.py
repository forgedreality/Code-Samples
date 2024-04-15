# bitwise XOR
# return the number of bits needed to flip to convert input a -> b
def bitswaprequired(a, b):
    count = 0
    c = a ^ b
    while(c != 0):
        count += c & 1
        c = c >> 1
    return count


print(bitswaprequired(12, 7))

# OUTPUT = 3
