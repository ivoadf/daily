class LinkedListElem:
    def __init__(self,value,next_elem):
        self.value = value
        self.next = next_elem
    def print(self):
        print(self.value, end=" ")
        if self.next is not None:
            self.next.print()
        else:
            print("")

def reverse_ll_rec(curr, prev):
    if curr is None:
        return prev
    t = reverse_ll_rec(curr.next, curr)
    curr.next = prev
    return t


def reverse_ll_ite(root):
    curr = root
    next = root.next
    root.next = None
    while next is not None:
        tmp = next.next
        next.next = curr
        curr = next
        next = tmp
    return curr
















# def reverse_ll_rec(elem,prev_elem):
#     if elem is None:
#         return prev_elem
#     root = reverse_ll_rec(elem.next,elem)
#     elem.next = prev_elem
#     return root
#
# def reverse_ll_ite(elem):
#     next_ele = elem.next
#     elem.next = None
#     current = elem
#     while next_ele is not None:
#         tmp = next_ele.next
#         next_ele.next = current
#         current = next_ele
#         next_ele = tmp
#     return current


root = LinkedListElem(0,LinkedListElem(1,LinkedListElem(2,LinkedListElem(3,None))))
root.print()
root = reverse_ll_rec(root,None)
root.print()

root = LinkedListElem(0,LinkedListElem(1,LinkedListElem(2,LinkedListElem(3,None))))
root.print()
root = reverse_ll_ite(root)
root.print()
