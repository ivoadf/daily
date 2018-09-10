""" In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA

[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]

Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A). """


node_letters = 'ABACA'

edges =[(0, 1),
        (0, 2),
        (2, 3),
        (3, 4)]

def get_max_val(root,letters,edges):
    def verify_max_path(active_branch,max_path_val,max_path):
        letter_array = [l for l in letters]
        letter_map = {}
        for (letter,active) in zip(letter_array,active_branch):
            if active:
                if letter in letter_map:
                    letter_map[letter] += 1
                else:
                    letter_map[letter] = 1
        for _,v in letter_map.items():
            if v > max_path_val:
                for i in range(len(max_path)):
                    max_path[i] = active_branch[i] #can't copy else outer scope loses reference to the object


    def helper(node,visited,active_branch,max_path_val,max_path):
        visited[node] = True
        active_branch[node] = True
        verify_max_path(active_branch,max_path_val,max_path)
        for (origin,dest) in edges:
            if origin == node:
                if not visited[dest]:
                    if helper(dest,visited,active_branch,max_path_val,max_path):
                        return True
                elif active_branch[dest]:
                    return True
        active_branch[node] = False
        return False
    
    visited = [False]*len(letters)
    active_branch = [False]*len(letters)
    max_path_val = 0
    max_path = [False]*len(letters)
    if helper(root,visited,active_branch,max_path_val,max_path):
        print("Graph contains cycle")
    else:
        print("Best value path: ",[l for i,l in enumerate(letters) if max_path[i]])

get_max_val(0,node_letters,edges)


