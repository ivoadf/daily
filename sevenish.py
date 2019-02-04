"""
N | binary representation
1 - 001
2 - 010
3 - 011
4 - 100
5 - 101
6 - 110
7 - 111

x | x | x => 7^2 | 7^1 | 7^0

N=7
7 => 111 => 7^2+7^1+7^0
"""

def n_sevenish(n):
    counter = 0
    sum = 0
    while (1 << counter) <= n:
        if (n & 1 << counter) != 0:
            sum += 7**counter
        counter += 1
    return sum

print(n_sevenish(1))#1
print(n_sevenish(2))#7
print(n_sevenish(3))#8
print(n_sevenish(4))#49
print(n_sevenish(7))#57
