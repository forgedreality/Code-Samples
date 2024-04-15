# Minimum Bribes
# https://www.hackerrank.com/challenges/new-year-chaos/problem

# Example description:
'''
    def minimumbribes(q):
        #
        # initialize the number of moves
        moves = 0 
        #
        # decrease Q by 1 to make index-matching more intuitive
        # so that our values go from 0 to N-1, just like our
        # indices.  (Not necessary but makes it easier to
        # understand.)
        q = [p-1 for p in q]
        #
        # Loop through each person (P) in the queue (Q)
        for i,p in enumerate(q):
            # i is the current position of P, while P is the
            # original position of P.
            #
            # First check if any P is more than two ahead of 
            # its original position
            if p - i > 2:
                print("Too chaotic")
                return
            #
            # From here on out, we don't care if P has moved
            # forwards, it is better to count how many times
            # P has RECEIVED a bribe, by looking at who is
            # ahead of P.  P's original position is the value
            # of P.
            # Anyone who bribed P cannot get to higher than
            # one position in front if P's original position,
            # so we need to look from one position in front
            # of P's original position to one in front of P's
            # current position, and see how many of those 
            # positions in Q contain a number large than P.
            # In other words we will look from P-1 to i-1,
            # which in Python is range(P-1,i-1+1), or simply
            # range(P-1,i).  To make sure we don't try an
            # index less than zero, replace P-1 with
            # max(P-1,0)
            for j in range(max(p-1,0),i):
                if q[j] > p:
                    moves += 1
        print(moves)
'''

def minimumBribes(q):
    # ensure indexes match expected positions (0-based)
    q = [p-1 for p in q]
    # initialize bribes count
    bribes = 0
    # iterate over indices and values
    for i,p in enumerate(q):
        # if the current has moved more than two positions
        # break and return 'Too chaotic'
        if p - i > 2:
            print ('Too chaotic')
            return

        # count how many people bribed the person in front of them
        # max ensures we don't check the guy outside 0th position
        for x in range(max(p - 1, 0), i):
            if q[x] > p:
                # if we moved, let's add one
                bribes += 1
    # output our result
    print(bribes)

minimumBribes([2, 1, 5, 3, 4])
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
