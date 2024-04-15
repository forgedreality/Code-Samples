def solution(n, firstNumber):
    y = firstNumber + (180 // (360 // n))
    return y if y <= n else y - n

print(solution(10, 7))