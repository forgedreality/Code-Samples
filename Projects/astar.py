import heapq

# The cost of moving from one node to another
# (in this example, we assume all moves have equal cost)
MOVE_COST = 1

# The heuristic function estimates the cost of getting from a given node
# to the goal node. In this example, we use the Manhattan distance.
def heuristic(a, b):
  (x1, y1) = a
  (x2, y2) = b
  return abs(x1 - x2) + abs(y1 - y2)

def a_star(graph, start, goal):
  # Create a priority queue to store the nodes that we visit
  queue = []
  
  # Push the start node onto the queue with a priority of 0
  heapq.heappush(queue, (0, start))
  
  # Create a dictionary to store the cost of getting from the start node to
  # each node that we visit
  cost_so_far = {start: 0}
  
  # Create a dictionary to store the previous node for each node that we visit
  # (we will use this to reconstruct the path to the goal after the search is complete)
  came_from = {}
  
  # Create a dictionary to store the estimated cost of getting from each node
  # to the goal (the cost of getting from the start node to the node, plus the
  # heuristic cost of getting from the node to the goal)
  # We use this to prioritize the nodes that we visit next.
  priority = {start: 0}
  
  while queue:
    # Pop the node with the lowest priority (estimated cost) from the queue
    current_cost, current_node = heapq.heappop(queue)
    
    # If the current node is the goal node, we have found a path to the goal
    if current_node == goal:
      break
    
    # Otherwise, visit each of the current node's neighbors
    for next_node in graph.neighbors(current_node):
      # Calculate the cost of getting to this neighbor from the start
      new_cost = cost_so_far[current_node] + MOVE_COST
      
      # If we haven't seen this neighbor before, or if the new cost to reach
      # this neighbor is lower than the previous cost, update the cost of
      # getting to this neighbor and set the neighbor's previous node
      if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
        cost_so_far[next_node] = new_cost
        priority[next_node] = new_cost + heuristic(goal, next_node)
        came_from[next_node] = current_node
        heapq.heappush(queue, (priority[next_node], next_node))
        
  # Create a list to store the final path
  path = []
  
  # Starting from the goal node, follow the `came_from` pointers back to the start
  # to reconstruct the path
  node = goal
  while node != start:
    path.append(node)
    node = came_from[node]
    
  # Add the start node to the path
  path.append(start)
  
  # Reverse the path so that it starts at the start node
  path = path[::-1]
  
  # Return the path and the cost of getting to the goal
  return path, cost_so_far[goal]


grid = [
    [4, 10, 15, 69, 73],
    [7, 16, 86, 6, 59],
    [8, 17, 91, 1, 23],
    [11, 21, 13, 90, 35],
    [73, 2, 3, 19, 65]
]
start_node = (2, 1)
end_node = (3, 4)

print(a_star(grid, start_node, end_node))
