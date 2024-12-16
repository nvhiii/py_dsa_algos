#  Quadratic Equation Solver
# Write a function that takes three coefficients a, b, and c of a quadratic equation (ax^2 + bx + c = 0) and returns:

# The two real roots if they exist.
# "No real roots" if the equation has complex roots.
# Use conditionals to check the discriminant (b^2 - 4ac) to determine the nature of the roots.

from math import sqrt

def quadratic(a: int, b: int, c: int):
    discriminant = (b**2) - (4 * a * c)
    if discriminant < 0:
        return "No real roots"

    root_pos, root_neg = (-b + sqrt(discriminant)) / (2 * a), (-b - sqrt(discriminant)) / (2 * a)
    if root_pos.is_integer() and root_neg.is_integer():
        return (root_pos, root_neg)
    else:
        return "The roots are complex!"


num1 = 3
num2 = 25
num3 = 7
print(quadratic(num1, num2, num3))