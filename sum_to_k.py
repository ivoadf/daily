# 
# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

a = [10, 15, 3, 7, 10]
k = 17

# O(N^2)
# def sum_to_k(arr, k):
#     for i in range(len(a)):
#         for j in range(i, len(a)):
#             if arr[i]+arr[j] == k:
#                 return True
#     return False

# O(N)
def sum_to_k(arr, k):
    hashtable = {}
    for i in range(len(a)):
        hashtable[arr[i]] = 0
    for i in range(len(a)):
        if k-arr[i] in hashtable:
            return True
    return False

print(sum_to_k(a,k))