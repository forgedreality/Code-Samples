# Directed graph iteration

graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": [],
}


def hasPathDepthFirst(graph, src, dst):
    if src == dst:
        return True

    for neighbor in graph[src]:
        if hasPathDepthFirst(graph, neighbor, dst) is True:
            return True

    return False


print(hasPathDepthFirst(graph, "f", "k"))


def hasPathBreadthFirst(graph, src, dst):
    queue = [src]

    while len(queue) > 0:
        current = queue.pop(0)  # remove first element and return it
        if current == dst:
            return True

        for neighbor in graph[current]:
            queue.append(neighbor)

    return False


print(hasPathBreadthFirst(graph, "f", "k"))


# Undirected graph iteration

undirectedDepthFirst_edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

def buildGraph(edges):
    graph = {}

    for edge in edges:
        [a, b] = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].insert(len(graph[a]), b)
        graph[b].insert(len(graph[b]), a)

    return graph


def hasPath(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False

    visited.add(src)

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst, visited) is True:
            return True

    return False


def undirectedDepthFirst(edges, src, dst, visited = {}):
    graph = buildGraph(edges)
    return hasPath(graph, src, dst, set())


print(undirectedDepthFirst(undirectedDepthFirst_edges, "i", "o"))


# Get total components #

def explore(graph, current, visited):
    if str(current) in visited:
        return False

    visited.add(str(current))

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True


def connectedComponentsCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited) is True:
            count += 1

    return count


print(connectedComponentsCount({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}))


# Linear traversal, return max component size #

def exploreSize(graph, node, visited):
    if str(node) in visited:
        return 0

    visited.add(str(node))

    size = 1
    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)

    return size


def largestComponent(graph):
    visited = set()
    longest = 0
    for node in graph:
        size = exploreSize(graph, node, visited)
        if size > longest:
            longest = size

    return longest


print(largestComponent({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}))


# Shortest graph path, breadth first traversal #

graph_edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]


def shortestPath(edges, src, dst):
    graph = buildGraph(edges)
    visited = set([src])
    queue = [[src, 0]]

    while len(queue) > 0:
        [node, distance] = queue.pop(0)  # remove first element and return it

        if node == dst:
            return distance

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                # add to end of list
                queue.insert(len(queue), [neighbor, distance + 1])

    return -1


print(shortestPath(graph_edges, "w", "y"))
