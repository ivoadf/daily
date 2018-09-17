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

lists = []
lists.append(LinkedListElem(5,LinkedListElem(7,LinkedListElem(11,None))))
lists.append(LinkedListElem(2,LinkedListElem(20,LinkedListElem(21,None))))
lists.append(LinkedListElem(4,LinkedListElem(6,LinkedListElem(15,LinkedListElem(18,None)))))

def merge_k_ll(lists):
    root = LinkedListElem(-1,None)
    merged_current_elem = root
    current_elems = lists
    while len([e for e in current_elems if e is not None]) > 0:
        minimum = (1000,-1) #(val,idx)
        for i,val in enumerate(current_elems):
            if val is not None and val.value < minimum[0]:
                minimum = (val.value,i)
        current_elems[minimum[1]] = current_elems[minimum[1]].next
        merged_current_elem.value = minimum[0]
        if len([e for e in current_elems if e is not None]) > 0:
            new_elem = LinkedListElem(-1,None)
            merged_current_elem.next = new_elem
            merged_current_elem = new_elem
    return root

r = merge_k_ll(lists)
r.print()
