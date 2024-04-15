# island count

islandMap = [
    ["W", "L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "L", "W", "L", "L", "W"],
    ["W", "W", "W", "W", "W", "W"],
]


def exploreGrid(grid, row, col, visited):
    rowInBounds = 0 <= row and row < len(grid)
    colInBounds = 0 <= col and col < len(grid[0])

    if not rowInBounds or not colInBounds:
        return False

    if grid[row][col] == "W":
        return False

    pos = f"{row},{col}"
    if pos in visited:
        return False

    visited.add(pos)

    exploreGrid(grid, row - 1, col, visited)
    exploreGrid(grid, row + 1, col, visited)
    exploreGrid(grid, row, col - 1, visited)
    exploreGrid(grid, row, col + 1, visited)

    return True


def islandCount(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if exploreGrid(grid, row, col, visited) is True:
                count += 1

    return count


print(islandCount(islandMap))


# min island size

islandSizeMap = [
    ["W", "L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "L", "W", "L", "L", "W"],
    ["W", "W", "W", "W", "W", "W"],
]


def exploreIslandSize(grid, row, col, visited):
    rowInBounds = 0 <= row and row < len(grid)
    colInBounds = 0 <= col and col < len(grid[0])

    if not rowInBounds or not colInBounds:
        return 0

    if grid[row][col] == "W":
        return 0

    pos = str(row) + "," + str(col)
    if pos in visited:
        return 0

    visited.add(pos)

    size = 1
    size += exploreIslandSize(grid, row - 1, col, visited)
    size += exploreIslandSize(grid, row + 1, col, visited)
    size += exploreIslandSize(grid, row, col - 1, visited)
    size += exploreIslandSize(grid, row, col + 1, visited)

    return size


def minIslandSize(grid):
    visited = set()
    minSize = float('inf')
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            size = exploreIslandSize(grid, row, col, visited)
            if size > 0 and size < minSize:
                minSize = size

    return minSize


print(minIslandSize(islandSizeMap))
