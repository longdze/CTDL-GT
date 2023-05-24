class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

#Kiem tra xem ngan xep co rong khong
    def is_emty(self):
        return self.top is None

#Thêm một phần tử mới vào đỉnh ngăn xếp
    def push(self, data):
        new_node = Node(data)
        if self.is_emty():
            self.top = new_node

#Lấy phần tử ở đỉnh của ngăn xếp và xóa nó khỏi ngăn xếp, trả về giá trị của phần tử đó
    def pop(self):
        if self.is_emty():
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data
#Xem phần tử ở đỉnh ngăn xếp mà không xóa nó, trả về giá trị của phần tử đó
    def peek(self):
        if self.is_emty():
            return None
        return self.top.data

#tạo đối tượng ngăn xếp
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())
print(stack.is_emty())