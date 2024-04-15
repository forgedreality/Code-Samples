# Angry Professor
# https://www.hackerrank.com/challenges/angry-professor/problem

def angryProfessor(k, a):
    t = 0
    for i in a:
        t += 1 if i <= 0 else 0
    return "NO" if t >= k else "YES"


print(angryProfessor(10, 10))