class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        # Thêm cạnh từ đỉnh nguồn đến đỉnh đích
        self.adj_list[src].append(dest)
        # Thêm cạnh từ đỉnh đích đến đỉnh nguồn (vì đồ thị vô hướng)
        self.adj_list[dest].append(src)

    def print_graph(self):
        for v in range(self.num_vertices):
            print("Đỉnh", v, ":", end=" ")
            for neighbor in self.adj_list[v]:
                print(neighbor, end=" ")
            print()

# Tạo một đơn đồ thị vô hướng với 5 đỉnh
graph = Graph(5)
# Thêm các cạnh vào đồ thị
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

# In đồ thị
graph.print_graph()
