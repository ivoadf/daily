""" Given an array of numbers, find the length of the longest increasing subsequence in the array. 
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15. """

a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

def longest(a):
    longest_path_to_i = [1]*len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[i] > a[j]:
                longest_path_to_i[i] = max(longest_path_to_i[i],longest_path_to_i[j]+1)
    return max(longest_path_to_i)

print(longest(a))#6