# Graph iteration

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}


def breadthFirstPrint(graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)  # removes first element, and returns it
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)


print("Breadth First:")
breadthFirstPrint(graph, "a")


def depthFirstPrint(graph, source):
    # recursive
    print(source)
    for neighbor in graph[source]:
        depthFirstPrint(graph, neighbor)

    # iterative
    '''
    queue = [source]
    while len(queue) > 0:
        current = queue.pop()  # removes last element, and returns it
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)
    '''


print("Depth First:")
depthFirstPrint(graph, "a")
