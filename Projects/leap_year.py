# Is leap year
# https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    leap = year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    
    '''    
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    '''
    return leap

year = 2100
print(is_leap(year))