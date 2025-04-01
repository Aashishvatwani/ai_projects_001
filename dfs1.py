def dfs_with_stack(graph, start):
    # Create a set to keep track of visited nodes
    visited = set()
    # Initialize the stack with the start node
    stack = [start]
    
    while stack:
        # Pop a node from the stack
        current_node = stack.pop()
        if current_node not in visited:
            # Mark the node as visited
            visited.add(current_node)
            print(current_node, end=" ")  # Process the node (print it in this case)
            
            # Add all unvisited neighbors to the stack
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example input graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run DFS starting from node 'A'
dfs_with_stack(graph, 'A')
