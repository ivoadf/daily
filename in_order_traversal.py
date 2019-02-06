"""
Depth First Traversals:
(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right)
(c) Postorder (Left, Right, Root)

This problem was asked by Palantir.

Typically, an implementation of in-order traversal of a binary tree has O(h) space complexity,
where h is the height of the tree. Write a program to compute the in-order traversal of
a binary tree using O(1) space.
"""
class BinaryElem:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def print(self):
        print(self.value, end=" ")

def in_order_traversal(root):
    cur = root
    while cur != None:
        if cur.left != None:
             pre = cur.left
             while pre.right != None and pre.right != cur:
                 pre = pre.right
             if pre.right == None:
                 pre.right = cur
                 cur = cur.left
             elif pre.right == cur:
                 pre.right = None
                 print(cur.value, end=" ")
                 cur = cur.right
        else:
           print(cur.value, end=" ")
           cur = cur.right


root = BinaryElem(1,BinaryElem(2, BinaryElem(4, None, None), BinaryElem(5, None, None)),BinaryElem(3, None, None))
print(in_order_traversal(root))
