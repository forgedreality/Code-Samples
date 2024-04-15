# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

def hackerrankInString(s):
    # Pop off start of list method
    # if we remove all chars, we found our word
    search = list('hackerrank')
    l = len(search)

    if len(s) < l:
        return 'NO'

    for i in s:
        if search and search[0] == i:
            search.pop(0)

        if len(search) == 0:
            return 'YES'

    return 'NO'

    # Counter method
    # If we find a char, we increment our count var, then check its length
    # search = 'hackerrank'
    # l = len(search)

    # if len(s) < l:
    #     return 'NO'

    # pos = 0
    # for i in s:
    #     if l - pos > len(s) - pos:
    #         return 'NO'

    #     if i == search[pos]:
    #         pos += 1

    #     if l == pos:
    #         return 'YES'

    # return 'NO'


for s in ['knarrekcah', 'hackerrank', 'hackeronek', 'abcdefghijklmnopqrstuvwxyz', 'rhackerank', 'ahankercka', 'hacakaeararanaka', 'hhhhaaaaackkkkerrrrrrrrank', 'crackerhackerknar', 'hhhackkerbanker']:
    print(hackerrankInString(s))
