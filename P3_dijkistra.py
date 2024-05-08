# Implement Greedy search algorithm for: Dijkstra's Minimal Spanning Tree Algorithm

import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary to keep track of shortest distances from start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Initialize priority queue (min heap) with starting node and its distance
    pq = [(0, start)]
    
    while pq:
        # Pop node with smallest distance from priority queue
        current_distance, current_node = heapq.heappop(pq)
        
        # If current distance to current node is greater than already known distance, skip
        if current_distance > distances[current_node]:
            continue
        
        # Update distances for neighbors of current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example graph (weighted directed graph)
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'C': 5, 'D': 1}
}

start_node = 'A'  # Example start node

shortest_distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node, ":")
for node, distance in shortest_distances.items():
    print(node, "-", distance)
