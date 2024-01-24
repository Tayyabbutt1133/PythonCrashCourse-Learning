# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1
# factorial(n)= n * factorial(n-1)

# Mathematical calculations (e.g., factorials, Fibonacci sequences).
# Tree and graph traversals.
# Sorting algorithms (e.g., merge sort, quicksort).
# Backtracking algorithms.
# Dynamic programming and memoization.
# Divide and conquer strategies.
# Fractal generation and intricate pattern creation.
# Expression parsing (e.g., recursive descent parsing).
# Simulation and simulation reduction.
# Manipulating certain data structures (e.g., linked lists, trees).



# actually runs like a loop in some sense

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        # Recursively calling function itself
        return n * factorial(n-1)
    
print(factorial(3)) #6
print(factorial(4)) #24
print(factorial(5)) #120
    
    