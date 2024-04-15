# Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem
# Find all substrings starting with vowels and consonants
vowels = 'aeiou'

'''
def update_dict(d, s):
    c = 0 if s not in d else d[s]
    d.update({s: c+1})
'''

def minion_game(string):
    #con = {}
    #vow = {}
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        if string[i].lower() in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    '''
    for c,v in enumerate(string):
        for l in range(c, len(string)):
            #print(l, len(string) - c, string[c:l+1])
            
            if v.lower() in vowels:
                kevin += 1
                #update_dict(vow, string[c:l+1])

            else:
                stuart += 1
                #update_dict(con, string[c:l+1])
    '''

    print(f'Stuart {stuart}' if stuart > kevin else (f'Kevin {kevin}') if kevin > stuart else 'Draw')

minion_game('adbhjsozjuifrtehuidmgosaanbc')