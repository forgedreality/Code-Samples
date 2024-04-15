# remove islands that aren't attached to the border
# 1 = land, 0 = water

matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

def checkSurroundings(matrix, row, col):
    queue = [[row, col]]
    visited = set()

    while len(queue) > 0:
        d = queue.pop(0)
        r, c = d[0], d[1]

        if str(r) + ',' + str(c) in visited:
            continue

        visited.add(str(r) + ',' + str(c))

        directions = [
            [r - 1, c], # up
            [r + 1, c], # dn
            [r, c - 1], # left
            [r, c + 1]  # right
        ]

        for d in directions:
            # if direction is out of bounds, node is a zero, or we've visited node before, skip it
            if d[0] < 0 or d[0] >= len(matrix) or d[1] < 0 or d[1] >= len(matrix[0]) or matrix[d[0]][d[1]] == 0 or str(d[0]) + ',' + str(d[1]) in visited:
                continue

            if d[0] == 0 or d[0] == len(matrix) - 1 or d[1] == 0 or d[1] == len(matrix[0]) - 1:
                return True

            queue.insert(0, d)

    return False

# remove islands (adjacent nodes consisting of 1s) which are not connected to the edges
def removeIslands(matrix):
    edgeConnected = False

    for row, row_value in enumerate(matrix):
        for col, col_value in enumerate(row_value):
            # ignore edges
            if row == 0 or row == len(matrix) - 1:
                break
            if col == 0 or col == len(matrix[0]) - 1:
                continue

            if col_value == 0:
                continue

            edgeConnected = checkSurroundings(matrix, row, col)
            if edgeConnected:
                continue

            matrix[row][col] = 0

    return matrix


print(removeIslands(matrix))


# ----------------------------- #
def checkMatch(pattern, grid, row, col):
    for i, r in enumerate(pattern):
        for j, c in enumerate(r):
            if row + i > len(grid) - 1 or col + j > len(grid[0]) - 1 or grid[row + i][col + j] != c:
                return 'NO'
    return 'YES'

def gridSearch(G, P):
    matched = 'NO'

    for i_r, row in enumerate(G):
        for i_c, col in enumerate(row):
            if col == P[0][0]:
                matched = checkMatch(P, G, i_r, i_c)
                if matched == 'YES':
                    return matched

    return matched


search_grid = [
    '7283455864',
    '6731158619',
    '8988242643',
    '3830589324',
    '2229505813',
    '5633845374',
    '6473530293',
    '7053106601',
    '0834282956',
    '4607924137'
]

search_pattern = [
    '9505',
    '3845',
    '3530'
]

'''
search_grid = [
'123412',
'561212',
'123634',
'781288'
]

search_pattern = [
    '12',
    '34'
]
'''

print(gridSearch(search_grid, search_pattern))
