#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

a = [3, 4, -1, 1]


def splitPosNeg(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
            t += 1
    return arr, j


def findMinPos(posArr):
    for i in range(len(posArr)):
        if abs(posArr[i])-1 < len(posArr) and posArr[abs(posArr[i])-1] > 0:
            posArr[abs(posArr[i])-1] = -posArr[abs(posArr[i])-1]
    for i in range(len(posArr)):
        if posArr[i] > 0:
            return i+1
    return len(posArr)+1


def findPos(a):
    a, i = splitPosNeg(a)
    return findMinPos(a[i:])


print(findPos(a))
