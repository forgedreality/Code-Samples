# run from commandline: py primes.py
def prime_number():
    primes = []
    # primes_2 = []
    low = int(input("What number would you like to start at? "))
    high = int(input("What number would you like to go up to? "))
    if int(low) == 1 or int(high) == 1:
        print("1 isn't a prime number dumb dumb")
    elif high < 2:
        print("Don't be annoying")
    else:
        for x in range(int(low), int(high)):
            for i in range(2, x):
                if (x % i) == 0 and x != i:
                    break
                elif (x % i) == 1 and i <= (x - 2):
                    continue
                elif (x % i) == 1 and i == (x - 1):
                    primes.append(x)
            x = x + 1
        print("The number of prime numbers is: ", len(primes))
        for y in range(2, int(low)):
            for z in range(2, y):
                if (y % z) == 0 and y != z:
                    break
                elif (y % z) == 1 and z <= (y - 2):
                    continue
                elif (y % z) == 1 and z == (y - 1):
                    primes_2.append(y)
            y = y + 1
        # if int(len(primes)) in primes or int(len(primes)) in primes_2:
        #     print("Huh, fancy that!", len(primes), "is also also a prime number!")
        print("The prime numbers are: ", primes)

prime_number()