import heapq

def astar_search(grid, start, goal):
    def heuristic(node):
        # Euclidean distance heuristic
        return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5

    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            # Goal reached, reconstruct the path
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from.get(current_node)
            return path[::-1]

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in get_neighbors(current_node):
            h = heuristic(neighbor)
            cost = current_cost + grid[neighbor[0]][neighbor[1]]
            total_cost = cost + h

            if neighbor not in visited or cost < h:
                heapq.heappush(priority_queue, (total_cost, neighbor))
                came_from[neighbor] = current_node

    return None  # No path found

def get_neighbors(node):
    x, y = node
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < len(grid) and 0 <= ny < len(grid[0])]

# Example grid
grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1]
]

start = (0, 0)
goal = (4, 4)

came_from = {}
path = astar_search(grid, start, goal)

if path:
    print("Shortest Path:", path)
else:
    print("No path found.")
