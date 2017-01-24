"""1. Write a function that will double any integer (n) and return the result"""
def double(n):
    n = int(n)*2
    return n
print(double(1890))


"""2.  Write a program that will (1) ask the user for an input value, (2) take
that and double it and  (3) print the result.
Include necessary print statements and address whitespace issues."""
print(double(input('Please enter a number to double and press enter.')))
