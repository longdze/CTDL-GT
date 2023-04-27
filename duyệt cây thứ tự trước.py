class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def thu_tu_truoc(node):
    if node:
        print(node.value)
        thu_tu_truoc(node.left)
        (node.right)(node.right)

#tạo cây
root = Node(1)
root.left = Node(2)
root.right = Node(3)

thu_tu_truoc(root)