# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
# https://www.geeksforgeeks.org/?p=25866
import random

def find_random(stream):
    res = stream[0]
    for i in range(1, len(stream)):
        j = random.randint(0,i)
        if j == 0:
            res = stream[i]
    return res

print(find_random([2,6,3,2,1,6]))