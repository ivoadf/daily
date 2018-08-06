# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
#

# one or two steps at a time

def fun1(N):
    if N < 0:
        return 0
    if N == 0:
        return 1
    return fun1(N-1) + fun1(N-2)

def fun2(N):
    w = [0]*(N+1)
    w[0] = 1
    w[1] = 1
    for i in range(2,N+1):
        w[i] = w[i-1]+w[i-2]
    return w[N]

print(fun1(4))
print(fun2(4))