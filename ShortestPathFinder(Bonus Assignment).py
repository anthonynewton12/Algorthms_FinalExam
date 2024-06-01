#Anthony Newton | Piedmont University | Algorithms | 3/19/2023
from collections import deque

def bfs_shortest_path(graph, start):
    # Create a queue for BFS and enqueue the starting node
    queue = deque([(start, [start])])
    # Create a set to keep track of visited nodes
    visited = set([start])
    # Create a dictionary to keep track of the shortest paths
    shortest_paths = {start: [start]}

    while queue:
        # Dequeue a vertex from queue and get its adjacent vertices
        (vertex, path) = queue.popleft()
        neighbors = graph[vertex]

        # Check each neighbor of the current vertex
        for neighbor in neighbors:
            if neighbor not in visited:
                # Mark the neighbor as visited and add it to the queue
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                # Update the shortest path to the neighbor
                shortest_paths[neighbor] = path + [neighbor]

    return shortest_paths
#Test Case
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'C', 'D'],
    'D': ['B']
}
#Finds the shortest path from 'A' to every other point
shortest_paths = bfs_shortest_path(graph, 'A')
print(shortest_paths)
