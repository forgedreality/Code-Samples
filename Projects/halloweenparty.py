# Halloween Party
# https://www.hackerrank.com/challenges/halloween-party/problem
import math

def halloweenParty(k):
    num1 = math.floor(k/2)
    num2 = k - num1
    return int(num1 * num2)

print(halloweenParty(10))