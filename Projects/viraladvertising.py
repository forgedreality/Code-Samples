# Viral Advertising
# https://www.hackerrank.com/challenges/strange-advertising/problem
import math

def viralAdvertising(n):
    liked = 2
    cu_liked = 2
    shared = liked * 3

    for _ in range(n - 1):
        liked = math.floor(shared / 2)
        shared = liked * 3
        cu_liked += liked
        print("D: ", cu_liked)
    return cu_liked

print(viralAdvertising(4))