
#The key purpose of a docstring in Python is to provide concise documentation within code, aiding in code understanding, usability, and maintenance. It serves as inline help, improves readability, supports interactive exploration, and facilitates testing and debugging.

# Python Comments
# Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

# Python docstrings
# As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

# We can access these docstrings using the doc attribute.

def cube(n):
    print(n)
    '''Takes in a number n, returns the cube of n'''
    print(n**3)
cube(5)
print(cube.__doc__)

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

print(square.__doc__)