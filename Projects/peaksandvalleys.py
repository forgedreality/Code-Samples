def breakingRecords(scores):
    high = scores[0]
    low = scores[0]

    peaks = 0
    valleys = 0

    for s in scores:
        if s > high:
            high = s
            peaks += 1
        elif s < low:
            low = s
            valleys += 1

    return([peaks, valleys])



print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
