#Alphabet Rangoli
#https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    chars = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = chars[size:x:-1]+chars[x:size]
        #print ("--"*x+ '-'.join(line)+"--"*x)
        print("-".join(line).center(4*(size-1)+1, "-"))
    '''
    chars = 'abcdefghijklmnopqrstuvwxyz-'
    midline = chars[-1] * (size * 2)
    count = size

    for i in range(size*2):
        if i % 2 != 0:
            continue
        count -= 1
        midline = midline[:i] + chars[count] + midline[i+1:]

    midline = midline[:-3] + midline[::-1]
    midpoint = len(midline)//2
    
    out = [midline]

    for _ in range(size-1):
        midline = '--' + midline[:midpoint] + midline[midpoint+4:] + '--'
        out.insert(0, midline)
        out.insert(len(out), midline)

    print('\n'.join(map(str, out)))
    '''

print_rangoli(2)