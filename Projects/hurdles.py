# hurdles

def hurdleRace(k, height):
    return(max(max(height) - k,0))


print(hurdleRace(4, [1, 6, 3, 5, 2]))