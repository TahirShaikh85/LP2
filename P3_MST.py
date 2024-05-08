# Implement Greedy search algorithm for Minimum Spanning Tree

import heapq

def prim(graph, start):
    # Initialize empty MST and set to keep track of visited vertices
    mst = []
    visited = set()
    
    # Initialize priority queue (min heap) with edges from starting vertex
    pq = [(weight, start, neighbor) for neighbor, weight in graph[start]]
    heapq.heapify(pq)
    
    # Mark start vertex as visited
    visited.add(start)
    
    # Iterate until priority queue is empty
    while pq:
        weight, src, dest = heapq.heappop(pq)
        # If destination vertex is not visited, add edge to MST and mark destination vertex as visited
        if dest not in visited:
            mst.append((src, dest, weight))
            visited.add(dest)
            # Add edges from destination vertex to priority queue
            for neighbor, edge_weight in graph[dest]:
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, dest, neighbor))
    
    return mst

# Example graph (weighted undirected graph represented as adjacency list)
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 2), ('E', 3)],
    'D': [('B', 1), ('C', 2), ('E', 1)],
    'E': [('C', 3), ('D', 1)]
}

# Choose starting vertex
start_vertex = 'A'

# Find Minimal Spanning Tree (MST)
mst = prim(graph, start_vertex)

print("Minimal Spanning Tree (MST):", mst)
