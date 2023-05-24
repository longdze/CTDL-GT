class Do_thi:
    def __init__(self):
        self.canh = []

    def them_canh(self, src, dest):
        # Thêm cạnh vào danh sách cạnh
        self.canh.append((src, dest))

    def in_do_thi(self):
        for canh in self.canh:
            src, dest = canh
            print("Cạnh:", src, "->", dest)

# Tạo một đa đồ thị có hướng
do_thi = Do_thi()
# Thêm các cạnh vào đồ thị
do_thi.them_canh(0, 1)
do_thi.them_canh(0, 1)  # Thêm cạnh lặp lại
do_thi.them_canh(1, 2)
do_thi.them_canh(2, 1)  # Thêm cạnh ngược lại
do_thi.them_canh(2, 3)
do_thi.them_canh(3, 0)

# In đồ thị
do_thi.in_do_thi()
