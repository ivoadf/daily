"""
Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
"""
import functools
def custom_sort(x, y):
    xy = int(str(x)+str(y))
    yx = int(str(y)+str(x))
    return xy-yx

cmp = functools.cmp_to_key(custom_sort)

def get_largest_number(list):
    # sort by last digit
    ordered_list = sorted(list, key=cmp, reverse=True)
    ordered_list = [str(i) for i in ordered_list]
    return "".join(ordered_list)

print(get_largest_number([10, 7, 76, 415])) #77641510
print(get_largest_number([54, 546, 548, 60])) #6054854654
