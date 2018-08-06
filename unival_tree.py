# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def number_unival(root):
    count, _ = number_unival_helper(root)
    return count


def number_unival_helper(root):
    if root is None:
        return 0, True
    else:
        left_c, left_u = number_unival_helper(root.left)
        right_c, right_u = number_unival_helper(root.right)
        total = left_c + right_c
        if left_u and right_u:
            if root.left is not None and root.left.val != root.val:
                return total, False
            if root.right is not None and root.right.val != root.val:
                return total, False
            return total + 1, True
        return total, False


tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

print(number_unival(tree)) #5