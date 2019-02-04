class BinaryElem:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def print(self):
        print(self.value, end=" ")

def traverse_outer_ccw(root):
    root.print()
    traverse_left(root.left)
    traverse_middle_leafs(root.left)
    traverse_middle_leafs(root.right)
    traverse_right(root.right)

def traverse_left(root):
    if root is not None:
        if root.left is not None:
            root.print()
            traverse_left(root.left)
        elif root.right is not None:
            root.print()
            traverse_left(root.right)

def traverse_middle_leafs(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        root.print()
    else:
        traverse_middle_leafs(root.left)
        traverse_middle_leafs(root.right)

def traverse_right(root):
    if root is not None:
        if root.right is not None:
            traverse_right(root.right)
            root.print()
        elif root.left is not None:
            traverse_right(root.left)
            root.print()

root = BinaryElem(0,BinaryElem(1, BinaryElem(2, None, None), BinaryElem(3, None, None)),BinaryElem(4, BinaryElem(5, None, None), BinaryElem(6, None, None)))
traverse_outer_ccw(root)
print()
root = BinaryElem(0,BinaryElem(1,None,BinaryElem(2,None,None)), BinaryElem(3,None,BinaryElem(4,None,None)))
traverse_outer_ccw(root)
print()
root = BinaryElem(0,None, BinaryElem(2,BinaryElem(3, BinaryElem(4, BinaryElem(5, None,None), BinaryElem(6, None,None)), BinaryElem(7, None,None)),None))
traverse_outer_ccw(root)
