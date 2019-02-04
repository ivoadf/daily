class BinaryElem:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def print(self):
        print(self.value, end=" ")

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return count_leaves(root.left) + count_leaves(root.right)

root = BinaryElem(0,BinaryElem(1, BinaryElem(2, None, None), BinaryElem(3, None, None)),BinaryElem(4, BinaryElem(5, None, None), BinaryElem(6, None, None)))
print(count_leaves(root))
