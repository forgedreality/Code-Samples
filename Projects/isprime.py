# is prime?
def isPrime(num):
    if num == 2 or num == 3: return True
    if num < 2 or num % 2 == 0: return False
    if num < 9: return True
    if num % 3 == 0: return False
    r = int(num**0.5)

    f = 5
    while f <= r:
        if num % f == 0: return False
        if num % (f+2) == 0: return False
        f += 6
    return True


print(isPrime(69))

# for i in range(int(input())):
#     x = int(input())
#     print("Prime" if isPrime(x) else "Not prime")