# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Jane Street.
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
# Implement car and cdr.

def car(p):
    def return_first_el(a, b):
        return a
    return p(return_first_el)

def cdr(p):
    def return_last_el(a, b):
        return b
    return p(return_last_el)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))