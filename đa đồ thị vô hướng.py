class Graph:
    def __init__(self):
        self.edges = []

    def add_edge(self, src, dest):
        # Thêm cạnh vào danh sách cạnh
        self.edges.append((src, dest))

    def print_graph(self):
        for edge in self.edges:
            src, dest = edge
            print("Cạnh:", src, "-", dest)

# Tạo một đa đồ thị vô hướng
graph = Graph()
# Thêm các cạnh vào đồ thị
graph.add_edge(0, 1)
graph.add_edge(0, 1)  # Thêm cạnh lặp lại
graph.add_edge(1, 2)
graph.add_edge(2, 2)  # Thêm self-loop
graph.add_edge(2, 3)
graph.add_edge(3, 0)

# In đồ thị
graph.print_graph()
