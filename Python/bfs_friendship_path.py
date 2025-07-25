from collections import deque

def build_graph(pairs):
    """
    Build an undirected graph (dictionary) from a list of pairs.
    Each person is connected to the other in both directions.
    """
    graph = {}
    for a, b in pairs:
        # Add b to a's list of friends
        graph.setdefault(a, []).append(b)
        
        # Add a to b's list of friends (undirected)
        graph.setdefault(b, []).append(a)
    return graph

def bfs_path(graph, start, goal):
    """
    Find a path from start to goal using Breadth-First Search (BFS).
    BFS explores neighbors level by level.
    """
    visited = set()     # Keep track of visited nodes
    queue = deque([[start]])   # Queue of paths (start with one path containing start node)  
    
    while queue:
        path = queue.popleft()  # Get the first path in the queue
        node = path[-1]      # Get the last node from the path
        
        if node == goal:
            return path    #Found the goal, return the path
        
        if node not in visited:
            visited.add(node)   #Mark node as visited


            # Explore neighbors of the current node
            for neighbor in graph.get(node, []):
                new_path = list(path)   # Copy current path
                new_path.append(neighbor)   # Add neighbor to new path
                queue.append(new_path)     # Add new path to queue
    return None    #return None if no path exists

friendships = [("Alice", "Bob"), ("Bob", "Cathy"), ("Cathy", "Derek"), ("Derek", "Eva"), ("Frank", "George")]
graph = build_graph(friendships)

print("Graph:", graph)

path1 = bfs_path(graph, "Alice", "Eva")
path2 = bfs_path(graph, "Alice", "Frank")

print("Path from Alice to Eva:", path1 if path1 else "No connection")
print("Path from Alice to Frank:", path2 if path2 else "No connection")
