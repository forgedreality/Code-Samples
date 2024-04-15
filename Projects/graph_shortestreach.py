# Shortest Reach
# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
from queue import Queue

class Graph:
    def __init__(self, n_nodes):
        self.nodes = {x:[] for x in range(n_nodes)}
        self.edges = []

    def connect(self, x, y):
        edge = [x, y]
        self.edges.append([x, y])

    def build_relationships(self, edges):
        graph = self.nodes
        for edge in edges:
            [a, b] = edge

            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].insert(len(graph[a]), b)
            graph[b].insert(len(graph[b]), a)

        return graph

    def find_all_distances(self, start):
        graph = self.build_relationships(self.edges)
        q = Queue()
        distances = [-1 for i in range(len(graph))]
        unvisited = [i for i in range(len(self.nodes))]

        distances[start] = 0
        unvisited.remove(start)
        q.put(start)

        while not q.empty():
            node = q.get()
            children = self.nodes[node]
            height = distances[node]
            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    q.put(child)

        distances.pop(start)

        print(" ".join(map(str, distances)))

'''
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)
'''

#t = 2
#first = '4 2'
graph = Graph(4)
connections = ['1 2', '1 3']

for i in connections:
    x,y = [int(x) for x in i.split()]
    graph.connect(x - 1, y - 1)

startNode = 1
graph.find_all_distances(startNode - 1)
print(graph.edges)
