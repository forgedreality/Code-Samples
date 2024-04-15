def popfirst(l):
     l.reverse()
     p = l.pop()
     l.reverse()

     return p

# myList = [3, 4, 5, 6, 7, 8, 9]
# print(popfirst(myList), myList)


def findShortestPath(edges, nodeA, nodeB):
    # get a an adjacency list of the edges in the graph
    graph = buildGraph(edges)
    # keep a record of the nodes we've already considered
    visited = {nodeA}
     # keep a record of the nodes and their distance from the starting node
    queue = [[nodeA, 0]]

    # iterate over the queue to explore all connected nodes
    while len(queue) > 0:
        # take the first element off the top of the queue and return its values
        [node, distance] = popfirst(queue)

        # if we've reached our target node, return how far we traveled
        if node == nodeB: return distance

        # let's explore all the neighbors
        for neighbor in graph[node]:
            # if the neighbor hasn't been visited...
            if neighbor not in visited:
                # record that we visited this neighbor
                visited.add(neighbor)
                # put the neighbor on the end of the stack, and increase the distance
                queue.append([neighbor, distance+1])

    # we couldn't get there, so return -1
    return -1


# create adjacency list
def buildGraph(edges):
    # declare the graph object
    graph = {}

    # iterate over each input edge
    for edge in edges:
        # init the nodes
        [a, b] = edge
        # add the nodes to our graph if not already present
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []

        # draw a connection between our two nodes
        graph[a].append(b);
        graph[b].append(a);

    # pass back the result
    return graph;

edges = [
    ['A','B'],
    ['A','D'],
    ['B','E'],
    ['E','F'],
    ['F','C'],
    ['C','G'],
    ['G','E']
]

print(findShortestPath(edges, 'A', 'G'))
