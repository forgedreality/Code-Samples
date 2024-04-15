

#
# Complete the 'findTotalImbalance' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY rank as parameter.
#

'''
subs = []

def getSubs(arr, s, e):
    if e == len(arr):
        return
    elif s > e:
        return getSubs(arr, 0, e + 1)
    subs.append(arr[s:e+1])
    return getSubs(arr, s + 1, e)
'''
def findTotalImbalance(rank):
    # Dang, I must be overthinking this somehow.  Or underthinking.  :D
    '''
    getSubs(rank, 0, 0)
    print(subs)

    for s in subs:
        c = 0
        for h in range(len(s) - 1):
            if s[h + 1] - s[h] > 1:
                c += 1
        print(c)
    '''

    res = 0
    r = sorted(rank)
    n = len(r)

    for i in range(n - 1):
        if r[i + 1] - r[i] > 1:
            res += n - i - 1
        elif r[i + 1] - r[i] == 1:
            res += n - i - 2

    return res
    
    '''
    r = sorted(rank)
    imb = 0

    for i in range(len(r) - 1, -1, -1):
        for j in range(len(r) - 2, -1, -1):
            imb += 1 if r[i] - r[j] > 1 else 0
    return imb
    '''

    '''
    #bubble sort
    icount = 0
    print(icount, rank)
    for idx, r in enumerate(rank):
        for i in range(len(rank) - 1):
            if i < len(rank) - 1 and rank[i] > rank[i + 1]:
                rank[i], rank[i+1] = rank[i+1], rank[i]
                icount += 1
    print(icount, rank)
    '''

    '''
    ref_arr = sorted(rank)
    index_dict = {v: i for i,v in enumerate(rank)}
    swaps = 0

    for i,v in enumerate(rank):
        correct_value = ref_arr[i]

        if v != correct_value:
            swp_idx = index_dict[correct_value]
            # do the swap
            rank[swp_idx], rank[i] = rank[i], rank[swp_idx]
            # update reference dict
            index_dict[v] = swp_idx
            index_dict[correct_value] = i

            swaps += 1 if abs(v - correct_value) > 1 else 0
    return swaps
    '''

def main():
    rank_count = [4, 3, 1, 2]
    result = findTotalImbalance(rank_count)

    print(result)


if __name__ == '__main__':
    main()
