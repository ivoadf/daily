# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if root is None:
        return '-1'
    ret = ' '.join([root.val, serialize(root.left), serialize(root.right)])
    return ret


def deserialize(string):
    token_list = string.split()
    def deserialize_rec(index):
        if token_list[index] == '-1':
            return None, index
        value = token_list[index]
        left, index = deserialize_rec(index+1)
        right, index = deserialize_rec(index+1)
        return Node(value, left, right), index
    return deserialize_rec(0)[0]



node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print(serialize(deserialize(serialize(node))))
print(deserialize(serialize(node)).left.left.val == 'left.left')