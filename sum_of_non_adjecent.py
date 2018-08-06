#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Airbnb.
#
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?

a = [2, 4, 6, 2, 5] # 13
b = [5, -2, -7, 12, 2, 1] #18
c = [5, 1, 1, 5] #10

def sum_of_adj(l):
    inc = 0
    exl = 0
    for n in l:
        t = inc
        inc = exl + n
        exl = max(t, exl)
    if inc > exl:
        return inc
    else:
        return exl

print(sum_of_adj(a))
print(sum_of_adj(b))
print(sum_of_adj(c))