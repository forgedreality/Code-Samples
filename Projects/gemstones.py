# Gemstones
# https://www.hackerrank.com/challenges/gem-stones/problem
# There are WAY better ways to do this.  :(
def gemstones(arr):
    gems = {}
    # output = []
    for s in arr:
        for i in s:
            if i not in gems:
                gems[i] = [s]
            elif s not in gems[i]:
                gems[i].append(s)
    return sum(1 for o in gems.keys() if len(gems[o]) == len(arr))
    # for o in gems.keys():
    #     if len(gems[o]) == len(arr):
    #         output.append(o)

    # return(len(output))

print(gemstones({'abcdde', 'baccd', 'eeabg'}))