def solution(a, m, k):
    sumnums = []
    count = 0

    n = len(a)
    for x in range(n - (m-1)):
        sub = a[x : x+m]
        print(sub)
        for y in range(len(sub) - 1):
            numA, numB = sub[y], sub[y + 1]
            if numA == numB: continue

            if numA + numB == k:
                print(numA, numB)
                count += 1
                break 
            
    return count

a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7, 3]
m = 4
k = 10
print(solution(a, m, k))