class Graph:
    def __init__(self):
        # Dictionary to store adjacency list
        self.adj_list = {}

    def add_edge(self, v, w):
        # Add edge from v to w
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[v].append(w)

        # Add edge from w to v (because it's an undirected graph)
        if w not in self.adj_list:
            self.adj_list[w] = []
        self.adj_list[w].append(v)

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} --> {self.adj_list[vertex]}")

g = Graph()

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

g.print_graph()
