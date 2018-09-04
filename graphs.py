edges = [
    [0,4,0,0,0,0,0,8,0],
    [4,0,8,0,0,0,0,11,0],
    [0,8,0,7,0,0,0,0,2],
    [0,0,7,0,9,14,0,0,0],
    [0,0,0,9,0,10,0,0,0],
    [0,0,0,14,10,0,2,0,0],
    [0,0,0,0,0,2,0,1,6],
    [8,11,0,0,0,0,1,0,7],
    [0,0,2,0,0,0,6,7,0]
]

class Graph:
    def __init__(self,size):
        self.edges = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
    #search
    def breath_first(self):
        print("Breath First Search:")
        visited = [False for _ in range(self.size)]
        queue = [0]
        visited[0] = True
        while len(queue) != 0:
            current_node = queue.pop(0)
            print(current_node, end=" ")
            for i,v in enumerate(self.edges[current_node]):
                if v != 0 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print("")

    def depth_first(self):
        def depth_helper(self, current_node, visited):
            print(current_node, end=" ")
            visited[current_node] = True
            for i,v in enumerate(self.edges[current_node]):
                if v != 0 and not visited[i]:
                    depth_helper(self,i,visited)
        print("Depth First Search:")
        visited = [False for _ in range(self.size)]
        depth_helper(self,0,visited)
        print("")
    
    def depth_first_ite(self):
        print("Depth First Iterative Search:")
        visited = [False for _ in range(self.size)]
        stack = [0]
        visited[0] = True
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node, end=" ")
            for i,v in enumerate(self.edges[current_node]):
                if v != 0 and not visited[i]:
                    visited[i] = True
                    stack.append(i)
        print("")

    #shortest path
    def shortest_path_djikstra(self):
        #does not work in graphs with negative weights
        print("Shortest path djikstra")
        INF = 1000
        finalized_nodes = []
        distances = [INF]*self.size
        distances[0] = 0
        while len(finalized_nodes) < self.size:
            min_dist = INF
            min_dist_node = -1
            
            for n, val in enumerate(distances):
                if val < min_dist and n not in finalized_nodes:
                    min_dist_node = n
                    min_dist = val
            finalized_nodes.append(min_dist_node)
            for target, edge_cost in enumerate(self.edges[min_dist_node]):
               if edge_cost != 0:
                   new_distance = min_dist + edge_cost
                   if new_distance < distances[target]:
                    distances[target] = new_distance
        print("Distances: ",distances)

    def shortest_path_bellmanford(self):
        #works on graphs with negative weights
        print("Shortest path bellmanford")
        INF = 1000
        distances = [INF]*self.size
        distances[0] = 0
        for _ in range(self.size-1):
            for source in range(self.size):
                for dest in range(self.size):
                    if self.edges[source][dest] != 0:
                        if distances[dest] > distances[source]+self.edges[source][dest]:
                            distances[dest] = distances[source]+self.edges[source][dest]
        #verify if negative cycle exists
        for source in range(self.size):
                for dest in range(self.size):
                    if self.edges[source][dest] != 0:
                        if distances[dest] > distances[source]+self.edges[source][dest]:
                            print("Negative cycle")
        print("Distances: ",distances)
    #MST
    def min_spanning_tree_prim(self):
        print("Prim MST")
        total_mst = 0
        finalized_nodes = []
        INF = 1000
        shortest_edge = [INF]*self.size
        shortest_edge[0] = 0 #start at 0
        while len(finalized_nodes) < self.size:
            min_edge = INF
            min_edge_id = -1
            for i, val in enumerate(shortest_edge):
                if val < min_edge and i not in finalized_nodes:
                    min_edge = val
                    min_edge_id = i 
            print(min_edge)
            finalized_nodes.append(min_edge_id)
            total_mst += min_edge
            for dest, cost in enumerate(self.edges[min_edge_id]):
                if cost != 0 and shortest_edge[dest] > cost:
                    shortest_edge[dest] = cost
        print("Total MST cost: ",total_mst)

    def min_spanning_tree_kruskal(self):
        def get_edge_weight(size,edges,source,dest):
            return edges[source*size+dest]

        # A utility function to find the subset of an element i
        def find_parent(parent,i):
            if parent[i] == -1:
                return i
            if parent[i]!= -1:
                return find_parent(parent,parent[i])
 
        # A utility function to do union of two subsets
        def union(parent,x,y):
            x_set = find_parent(parent, x)
            y_set = find_parent(parent, y)
            parent[x_set] = y_set

        total_edges = []
        for a in self.edges:
            total_edges += a
        sorted_edge_ids = sorted(range(len(total_edges)), key=lambda k: total_edges[k])
        
        num_edges_in_tree = 0
        current_sorted_id = 0
        parent = [-1]*self.size #to check for cycles
        while num_edges_in_tree < self.size - 1:
            



    #Cycles
    def detect_cycle_with_dfs(self):
        visited = [False for _ in range(self.size)]
        stack = [0]
        visited[0] = True
        while len(stack) > 0:
            current_node = stack.pop()
            for i,v in enumerate(self.edges[current_node]):
                if v != 0 and not visited[i]:
                    visited[i] = True
                    stack.append(i)
                elif v != 0 and visited[i]:
                    return True
        return False

    def eulerian_circuit(self):
        pass
    #Flow
    def max_flow_fordfulkerson(self):
        pass
    def min_cut(self):
        pass
    #Hard problems
    def travelling_salesman(self):
        pass 
    def graph_coloring(self):
        pass

G = Graph(9)
G.edges = edges
G.breath_first()
G.depth_first()
G.depth_first_ite()
G.shortest_path_djikstra()
G.shortest_path_bellmanford()
G.min_spanning_tree_prim()