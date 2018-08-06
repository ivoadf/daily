# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
#
# Hint: The basic equation of a circle is x2 + y2 = r2.

import random

total_points = 0
inside_points = 0
for i in range(100000):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <= 1:
        inside_points += 1
    total_points += 1

print("Pi approximation: {}".format(4*inside_points/total_points))