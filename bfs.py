from collections import deque

def bfs(graph, start):
    # Create a set to keep track of visited nodes
    visited = set()
    # Create a queue for the BFS
    queue = deque([start])
    # Visit the start node
    visited.add(start)
    
    while queue:
        # Dequeue a node from the queue
        current_node = queue.popleft()
        print(current_node, end=" ")  # Process the node (print it in this case)
        
        # Visit all unvisited neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example input graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run BFS starting from node 'A'
bfs(graph, 'A')
