# Tuple cannot be changed while list can

# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.


# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing elements of a tuple
print("Tuple:", my_tuple)
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])
print("Slice of the tuple:", my_tuple[2:5])

# Tuple with different data types
mixed_tuple = (1, 'apple', 3.14, True)

# Nested tuple
nested_tuple = ((1, 2), ('a', 'b'), (True, False))

# Tuple packing and unpacking
packed_tuple = 1, 2, 'hello'
x, y, z = packed_tuple
print("Unpacked values:", x, y, z)
