#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
class Node:
    def __init__(self):
        self.children = {}

def add_string(root, string):
    if len(string) == 0:
        return root
    if string[0] in root.children:
        add_string(root.children[string[0]],string[1:])
    else:
        root.children[string[0]] = Node()
        add_string(root.children[string[0]],string[1:])

def sub_word_list(root):
    if len(root.children) == 0:
        return []
    total = []
    for c, node in root.children.items():
        w_l = sub_word_list(node)
        if len(w_l)==0:
            total += [c]
        else:
            total += [c+w for w in w_l]
    return total

def search_string(root, string):
    if len(string) == 0:
        return sub_word_list(root)
    if string[0] in root.children:
        return [string[0] + w for w in search_string(root.children[string[0]],string[1:])]
    else:
        return []



def autocomplete(s, l):
    root = Node()
    for w in l:
        add_string(root, w)
    return search_string(root,s)


print(autocomplete('de',['dog','deer','deal']))