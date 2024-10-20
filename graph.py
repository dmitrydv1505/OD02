# Граф можно представить в виде списка смежности,
# где каждый элемент списка содержит узел и список соседних узлов.

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def get_vertices(self):
        return list(self.adjacency_list.keys())

    def get_edges(self):
        edges = []
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                if (neighbor, vertex) not in edges:
                    edges.append((vertex, neighbor))
        return edges

# Пример использования
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(1, 2)
graph.add_edge(1, 3)