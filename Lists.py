marks=[1,2,3,4,5,6,7,8,9,10]

print(marks)
print(type(marks))

print("Marks of Ali Abdaal are: ",marks[0])
print("Marks of Tayyeb butt are: ",marks[1])
print("Marks of saqib Abdaal are: ",marks[2])
print("Marks of Ali shah are: ",marks[3])

# how we can check things from list
if "Tayeb" in marks:
    print("Yes Tayyeb is here")
else:
    print("No")
    
    
    print(marks)
    print(marks[0:2])
    print(marks[0:3:2])
    
    
    
    # List comprehension
    lst=[i*i for i in range(10)]
    print("List comprehension result: ",lst)
    
    
    
list=[i*i for i in range(10) if i%2==0]
print(list)
    
    
    
    
    
    
    
    
    
    