# Encryption
# https://www.hackerrank.com/challenges/encryption/problem
import math

def encryption(s):
    l = len(s)
    sq = math.sqrt(l)
    x = math.floor(sq)
    y = math.ceil(sq)

    #print(x,y)
    if x * y > l:
        x = y

    #o = [''] * y
    o = ''
    counter = 0

    '''
    for n in range(x):
        for m in range(y):
            o[m] +=  '' if counter > l - 1 else s[counter]
            counter += 1
    '''
    for i in range(y):
        o += s[i::y] + ' '

    #print(o)
    #return ''.join(o)
    return o

string = 'hellodogdoyouhaveadollar'
print(encryption(string))