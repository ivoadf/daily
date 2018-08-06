#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

a = [1,2,3,4,5]
# sol = [120, 60, 40, 30, 24]

# with division
def prod_all_div(arr):
    total = arr[0]
    for e in arr[1:]:
        total *= e
    new_arr = [0]*len(arr)
    for i in range(len(new_arr)):
        new_arr[i] = total/arr[i]
    return new_arr

#without division
def prod_all(arr):
    forward = [0]*len(arr)
    backward = [0]*len(arr)
    forward[0] = arr[0]
    for i in range(1,len(arr)):
        forward[i] = forward[i-1]*arr[i]
    backward[-1] = arr[-1]
    for i in range(len(arr)-2,-1,-1):
        backward[i] = backward[i+1]*arr[i]
    new_arr = [0]*len(arr)
    new_arr[0] = backward[1]
    new_arr[-1] = forward[-2]
    for i in range(1,len(new_arr)-1):
            new_arr[i] = forward[i-1]*backward[i+1]
    return new_arr
print(prod_all(a))