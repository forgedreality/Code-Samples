# return primes from first n fibonacci numbers

def isPrime(num):
    if num == 2 or num == 3: return True
    if num < 2 or num %2 == 0: return False
    if num < 9: return True
    if num % 3 == 0: return False
    r = int(num**0.5)
    f = 5
    while f <= r:
        if num % f == 0: return False
        if num % (f+2) == 0: return False
        f += 6
    return True


def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n - 1, memo) + fib_2(n - 2, memo)

    memo[n] = result
    return result


def fib(n):
    if n == 0:
        return 0
    memo = [None] * (n + 1)

    return fib_2(n, memo)


def solution(n):
    out = []
    fibs = []
    for i in range(1, n+1):
        fibs.append(fib(i))

    print(fibs)
    for i in fibs:
        if isPrime(i):
            out.append(i)

    return out

print(solution(10))