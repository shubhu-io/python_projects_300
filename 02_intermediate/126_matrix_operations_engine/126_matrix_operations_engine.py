"""
Project 126: Matrix Operations Engine
Category: Web & APIs
Description: Algorithmic engine implementing graph traversal, shortest path optimization, and step-by-step computation.
"""
import heapq

class GraphPathfinder126:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph: self.graph[u] = []
        if v not in self.graph: self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0
        pq = [(0, start_node)]

        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if current_dist > distances[current_node]:
                continue
            for neighbor, weight in self.graph[current_node]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances

def run_project_126():
    print("=" * 45)
    print("   PYTHON PROJECT 126: MATRIX OPERATIONS ENGINE")
    print("=" * 45)
    
    finder = GraphPathfinder126()
    finder.add_edge('A', 'B', 4)
    finder.add_edge('A', 'C', 2)
    finder.add_edge('B', 'C', 1)
    finder.add_edge('B', 'D', 5)
    finder.add_edge('C', 'D', 8)
    
    distances = finder.dijkstra('A')
    print("Shortest Path Distances from Node 'A':")
    for node, dist in sorted(distances.items()):
        print(f"  Node {node}: {dist} units")
    return True

if __name__ == "__main__":
    run_project_126()
