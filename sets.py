# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

# Removing duplicates from a list.
# Checking membership of an element.
# Performing mathematical operations like union, intersection, and difference.
# Efficient data lookup in large collections.
# Storing unique elements when order doesn't matter.
# Set operations in mathematical or algorithmic contexts.
# Ensuring hashability of elements.
# Removing redundancies in text processing.
# Finding unique elements in an iterable.
# Implementing algorithms that require a unique collection of elements.


info = {"Carla", 19, False, 5.9, 19}
print(info)

for items in info:
    print(items)
    
    
    # 1.Union
    # 2.Update
    #Methods to perform in sets 
    
    s1={1,2,3,4,5,6,7}
    s2={6,1,3,9,8,10}
    print("Union of s1 and s2 is:",s1.union(s2))
    print(s1,s2)
    s1.update(s2)
    print("After updating s1: ",s1)
    

print("Intersection of s1 and s2 is:",s1.intersection(s2))
    
print("The difference between of s1 and s2 is:",s1.difference(s2))
    
    
 # isdisjoint():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))


# issuperset():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))    
    
# issubset():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))


# clear():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# del
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities


# pop()
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities1.pop()
print(cities1)
print("After popping elements:",item)

# remove()/discard()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)


# update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# add()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)


















