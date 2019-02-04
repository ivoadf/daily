def subarray_sum(a, s):
    total = 0
    sum_hash = {}
    for i, elem in enumerate(a):
        total += elem
        if total == s:
            return (0, i)
        if total-s in sum_hash:
            return (sum_hash[total-s]+1,i)
        sum_hash[total] = i
    return (None,None)
































# def subarray_sum(a, s):
#     hash = {}
#     total = 0
#     for i, elem in enumerate(a):
#         total += elem
#         if total == s:
#             return (0, i)
#         if total-s in hash:
#             return (hash[total-s]+1, i) # if difference exists means that the subarray starting from where the hash[total-s] to current i sums to s. The difference in total -s is absorbed by the initial subarray [0:hash[total-s]]
#         hash[total] = i
#     return (None, None)


a1 = [1, 4, 20, 3, 10, 5]
print(subarray_sum(a1, 33)) #2-4
a2 = [10, 2, -2, -20, 10]
print(subarray_sum(a2, -10)) #0-3
