# https://www.hackerrank.com/challenges/merge-the-tools/problem

def getSubStrings(inputStr, length):
    return [inputStr[i:i + length] for i in range(0, len(inputStr) - (length - 1), length)]


def deDupeHelper(inputStr):
    tmp = ''

    for c in inputStr:
        if c in tmp:
            continue

        tmp = tmp + c

    return tmp


def merge_the_tools(string, k):
    sub_strings = getSubStrings(string, k)

    for i,s in enumerate(sub_strings):
        print(deDupeHelper(s))

    
merge_the_tools('AAABCADDE', 3)