#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
#
# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

class XOR_elem:
    def __init__(self, val, both):
        self.val = val
        self.both = both

class XOR_list:
    def __init__(self):
        self.root = None

    def add(self, elem):
        if self.root is None:
            self.root = XOR_elem(elem, 0)
        else:
            prev_addr = get_pointer(self.root)
            current_elem = dereference_pointer(self.root.both)
            next_addr = current_elem.both ^ prev_addr
            while next_addr != 0:
                prev_addr = get_pointer(current_elem)
                current_elem = dereference_pointer(next_addr)
                next_addr = current_elem.both ^ prev_addr
            newElem = XOR_elem(elem, get_pointer(current_elem))
            current_elem.both ^= get_pointer(newElem)

    def get(self, index):
        i = 0
        prev_addr = 0
        current_elem = dereference_pointer(self.root)
        while i != index:
            prev_addr_tmp = get_pointer(current_elem)
            current_elem = dereference_pointer(current_elem.both ^ prev_addr)
            prev_addr = prev_addr_tmp
        return current_elem
