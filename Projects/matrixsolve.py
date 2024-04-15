def formingMagicSquare(s):
    t = [
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    ]

    totals = []
    for row in t:
        cost = 0
        for t_row, s_row in zip(row, s):
            for x, y in zip(t_row, s_row):
                if not x == y:
                    cost += max([x, y]) - min([x, y])
        totals.append(cost)
    return min(totals)

print(formingMagicSquare([[ 4, 9, 2 ], [ 3, 2, 7 ], [ 8, 1, 5 ]]))