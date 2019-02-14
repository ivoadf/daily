"""
You are given N identical eggs and access to a building with k floors. Your task is to find the lowest floor that will
 cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks
  when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.
"""
MAX = 100000

def min_tries(n_eggs, k_floors):
    matrix = [[None]*n_eggs for _ in range(k_floors+1)] # KxN
    # n_eggs == 1,  tries = k_floors
    for k in range(k_floors+1):
        matrix[k][0] = k
    # k_floors == 0, tries = 0. k_floors == 1, tries = 1
    matrix[0] = [0]*n_eggs
    matrix[1] = [1]*n_eggs


    for n in range(1, n_eggs):
        for k in range(2, k_floors+1):
            matrix[k][n] = MAX
            for x in range(1, k):
                res = 1 + max(matrix[x-1][n-1], #egg breaks
                matrix[k-x][n]) #egg doens't break
                if res < matrix[k][n]:
                    matrix[k][n] = res

    return matrix[k_floors][n_eggs-1]


print(min_tries(1,5))# 5
print(min_tries(2,10))# 4
print(min_tries(2,36))# 8
