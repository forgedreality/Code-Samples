# returns True if input string is a palindrome
import math

def testString(s):
    return s[math.floor(len(s)/2):][::-1] == s[:math.floor(len(s)/2)] or s[math.floor(len(s)/2)+1:][::-1] == s[:math.floor(len(s)/2)]
    # print(s[math.ceil(len(s)/2):][::-1] == s[:math.ceil(len(s)/2)])

print(testString("racecar"))