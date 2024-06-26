# class Graph(object):

#     def __init__(self, graph_dict=None):
#         """ initializes a graph object
#             If no dictionary or None is given,
#             an empty dictionary will be used
#         """
#         if graph_dict == None:
#             graph_dict = {}
#         self._graph_dict = graph_dict

#     def edges(self, vertice):
#         """ returns a list of all the edges of a vertice"""
#         return self._graph_dict[vertice]

#     def all_vertices(self):
#         """ returns the vertices of a graph as a set """
#         return set(self._graph_dict.keys())

#     def all_edges(self):
#         """ returns the edges of a graph """
#         return self.__generate_edges()

#     def add_vertex(self, vertex):
#         """ If the vertex "vertex" is not in
#             self._graph_dict, a key "vertex" with an empty
#             list as a value is added to the dictionary.
#             Otherwise nothing has to be done.
#         """
#         if vertex not in self._graph_dict:
#             self._graph_dict[vertex] = []

#     def add_edge(self, edge):
#         """ assumes that edge is of type set, tuple or list;
#             between two vertices can be multiple edges!
#         """
#         edge = set(edge)
#         vertex1, vertex2 = tuple(edge)
#         for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
#             if x in self._graph_dict:
#                 self._graph_dict[x].add(y)
#             else:
#                 self._graph_dict[x] = [y]

#     def __generate_edges(self):
#         """ A static method generating the edges of the
#             graph "graph". Edges are represented as sets
#             with one (a loop back to the vertex) or two
#             vertices
#         """
#         edges = []
#         for vertex in self._graph_dict:
#             for neighbour in self._graph_dict[vertex]:
#                 if {neighbour, vertex} not in edges:
#                     edges.append({vertex, neighbour})
#         return edges

#     def __iter__(self):
#         self._iter_obj = iter(self._graph_dict)
#         return self._iter_obj

#     def __next__(self):
#         """ allows us to iterate over the vertices """
#         return next(self._iter_obj)

#     def __str__(self):
#         res = "vertices: "
#         for k in self._graph_dict:
#             res += str(k) + " "
#         res += "\nedges: "
#         for edge in self.__generate_edges():
#             res += str(edge) + " "
#         return res



# g = { "2" : {"1"},
#       "b" : {"2"},
#       "c" : {"b", "c", "d", "e"},
#       "d" : {"a", "c"},
#       "e" : {"c"},
#       "f" : {}
#     }



# graph = Graph(g)

# for vertice in graph:
#     print(f"Edges of vertice {vertice}: ", graph.edges(vertice))





def findCount(graph_nodes, graph_from, graph_to, graph_weight, minDistance, company):
    n = graph_nodes
    gf = graph_from
    gt = graph_to
    gw = graph_weight
    md = minDistance
    c = company


#     return(graph_nodes, graph_from, graph_to, graph_weight, minDistance, company)

# print(findCount(2, [1], [2], [5], 4, [1, 2]))
