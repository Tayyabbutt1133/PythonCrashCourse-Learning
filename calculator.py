# Calculator in Python with user input

# Take input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Ask the user for the operation
operation = input("Press 1 or 2 or 3 or 4")

# Perform the calculation based on the user's choice
if operation == "1":
    result = a + b
    print("By adding numbers", a, "+", b, "we get", result)
elif operation == "2":
    result = a - b
    print("By subtracting numbers", a, "-", b, "we get", result)
elif operation == "3":
    result = a * b
    print("By multiplying numbers", a, "*", b, "we get", result)
elif operation == "4":
    # Check for division by zero
    if b != 0:
        result = a / b
        print("By dividing numbers", a, "/", b, "we get", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose a valid operation.")

