# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
# implement a function rand5() that returns an integer from 1 to 5 (inclusive).

# for i in range(1,7):
#     for j in range(1,7):
#         print(7*i+j-7)

import random

def rand7():
    return random.randint(1,7)

def rand5():
    x = 7*rand7() + rand7() - 7
    if x < 41:
        return (x % 5)+1
    else:
        return rand5()

for _ in range(10):
    print(rand5())