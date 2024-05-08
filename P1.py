# Implement depth first search algorithm and Breadth First Search algorithm, Use an
# undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree datastructure

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=' ')
        for neighbor_vertex in self.graph[start_vertex]:
            if neighbor_vertex not in visited:
                self.dfs(neighbor_vertex, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=' ')
            for neighbor_vertex in self.graph[current_vertex]:
                if neighbor_vertex not in visited:
                    visited.add(neighbor_vertex)
                    queue.append(neighbor_vertex)

    def recursive_dfs(self):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                self._recursive_dfs_util(vertex, visited)

    def _recursive_dfs_util(self, start_vertex, visited):
        visited.add(start_vertex)
        print(start_vertex, end=' ')
        for neighbor_vertex in self.graph[start_vertex]:
            if neighbor_vertex not in visited:
                self._recursive_dfs_util(neighbor_vertex, visited)

    def recursive_bfs(self):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                self._recursive_bfs_util([vertex], visited)

    def _recursive_bfs_util(self, queue, visited):
        if not queue:
            return
        current_vertex = queue.pop(0)
        visited.add(current_vertex)
        print(current_vertex, end=' ')
        for neighbor_vertex in self.graph[current_vertex]:
            if neighbor_vertex not in visited:
                visited.add(neighbor_vertex)
                queue.append(neighbor_vertex)
        self._recursive_bfs_util(queue, visited)

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS:")
g.dfs(0)
print("\nBFS:")
g.bfs(0)

print("\nRecursive DFS:")
g.recursive_dfs()
print("\nRecursive BFS:")
g.recursive_bfs()
