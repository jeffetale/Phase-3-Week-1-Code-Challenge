"""
Challenge 2: Two numbers are positive.
Task:
Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three
 integers are positive numbers (greater than zero), and False - otherwise.
"""

def two_positive(a: int, b: int, c: int):
    return sum(x > 0 for x in (a, b, c)) == 2
print("Check if two numbers are positive.")
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Error: Please enter a valid integer value.')

a = get_integer('Enter the first integer: ')
b = get_integer('Enter the second integer: ')
c = get_integer('Enter the third integer: ')

result = two_positive(a, b, c)
print (f"Result: {result}")