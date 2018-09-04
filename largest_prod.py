# Good morning! Here's your coding interview problem for today.
# This problem was asked by Facebook.
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
# You can assume the list has at least three integers.

a = [-10, -10, 5, 2] #500
#sort array and chose max of a[n-3]*a[n-2]*a[n-1] or a[-1]*a[-2]*a[n-1]

#scan array and find 3 maxes and 3 mins
def largest(a):
    maxes = [0]*3
    mins = [0]*2
    for elem in a:
        if elem > maxes[0]:
            if elem > maxes[1]:
                if elem > maxes[2]:
                    maxes[0] = maxes[1]
                    maxes[1] = maxes[2]
                    maxes[2] = elem
                else:
                    maxes[0] = maxes[1]
                    maxes[1] = elem
            else:
                maxes[0] = elem
        if elem < mins[0]:
            if elem < mins[1]:
                mins[0] = mins[1]
                mins[1] = elem
            else:
                mins[0] = elem
    return max(maxes[0]*maxes[1]*maxes[2],maxes[2]*mins[0]*mins[1])

print(largest(a))