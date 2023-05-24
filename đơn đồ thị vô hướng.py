class Do_thi:
    def __init__(self, so_dinh):
        self.so_dinh = so_dinh
        self.adj_list = [[] for _ in range(so_dinh)]

    def them_canh(self, src, dest):
        # Thêm cạnh từ đỉnh nguồn đến đỉnh đích
        self.adj_list[src].append(dest)
        # Thêm cạnh từ đỉnh đích đến đỉnh nguồn (vì đồ thị vô hướng)
        self.adj_list[dest].append(src)

    def in_do_thi(self):
        for v in range(self.so_dinh):
            print("Đỉnh", v, ":", end=" ")
            for neighbor in self.adj_list[v]:
                print(neighbor, end=" ")
            print()

# Tạo một đơn đồ thị vô hướng với 5 đỉnh
do_thi = Do_thi(5)
# Thêm các cạnh vào đồ thị
do_thi.them_canh(0, 1)
do_thi.them_canh(0, 4)
do_thi.them_canh(1, 2)
do_thi.them_canh(1, 3)
do_thi.them_canh(1, 4)
do_thi.them_canh(2, 3)
do_thi.them_canh(3, 4)

# In đồ thị
do_thi.in_do_thi()
