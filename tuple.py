# Use when you want a collection that cannot change (immutable).
# Use tuples when you have a collection of items, and you don't want the data to be modified accidentally.
# # Example: Coordinates (latitude, longitude) that represent a fixed location.


# Tuple operations
my_tuple = (1, 2, 3)
# The following would result in an error because tuples are immutable
my_tuple.append(4)
my_tuple[0] = 0