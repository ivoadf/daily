def maxLen(arr):
    max_len = 0
    sum_hash = {}
    sum = 0
    for i, elem in enumerate(arr):
        sum += elem
        if sum == 0:
            max_len += 1
        if sum in sum_hash:
            max_len = max(i - sum_hash[sum], max_len)
        else:
            sum_hash[sum] = i
    return max_len



































# def maxLen(arr):
#     sum_hash = {}
#     result = 0
#     sum = 0
#     for i, elem in enumerate(arr):
#         sum += elem
#         if sum == 0:
#             result += 1
#         if sum in sum_hash:
#             result = max(i-sum_hash[sum], result)
#         else:
#             sum_hash[sum] = i
#     return result

print(maxLen([15, -2, 2, -8, 1, 7, 10, 23]))
print(maxLen([2, -2, 2, -2]))
