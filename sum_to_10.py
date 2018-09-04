# This problem was asked by Microsoft.
# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.
# For example, given 1, you should return 19. Given 2, you should return 28.
import math

def nth_perfect_number(n):
    perfect_counter = 1
    number_counter = 19
    while perfect_counter != n:
        number_counter += 1
        s = 0
        aux_number = number_counter
        while aux_number > 0:
            s += aux_number % 10
            aux_number = aux_number // 10
        if s == 10:
            perfect_counter += 1

    return number_counter
    

print(nth_perfect_number(1))
print(nth_perfect_number(2))
print(nth_perfect_number(10))

#If we take a closer look, we can notice that all multiples of 9 are present in arithmetic progression
def nth_perfect_number_opt(n):
    perfect_counter = 1
    number_counter = 19
    while perfect_counter != n:
        number_counter += 9
        s = 0
        aux_number = number_counter
        while aux_number > 0:
            s += aux_number % 10
            aux_number = aux_number // 10
        if s == 10:
            perfect_counter += 1

    return number_counter

print(nth_perfect_number_opt(1))
print(nth_perfect_number_opt(2))
print(nth_perfect_number_opt(10))