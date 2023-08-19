"""
Challenge 2: Two numbers are positive.
Task:
Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three
 integers are positive numbers (greater than zero), and False - otherwise.
"""

def two_positive(a: int, b: int, c: int):
    return sum(x > 0 for x in (a, b, c)) == 2

a = int(input('Enter the first integer: '))
b = int(input('Enter the second integer: '))
c = int(input('Enter the third integer: '))

result = two_positive(a, b, c)
print (result)