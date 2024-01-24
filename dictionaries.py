dic={
    "Tayyeb Age":19,
    "Year of born":2003,
    "Year name":"September"
}

print("Tayyeb age is:",dic["Tayyeb Age"])

Markslist={
    "Ali":7,
    "Tayyeb":10,
    "Uzain":6
}


askuser=input("Enter Student name to get marks:")
if(askuser=="Ali"):
    print(Markslist["Ali"])
elif(askuser=="Tayyeb"):
    print(Markslist["Tayyeb"])
else:
    print(Markslist["Uzain"])
    
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# Accessing single value
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

# Accessing multiple values
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# Accessing Keys 
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

# Dictionaries methods 


# 1.Update method  

emp1 ={ 123:54,456:99,423:87,112:97}

emp2={122:55,676:88}
print("Department 1 employee id:",emp1)
emp1.update(emp2)
print("Updated department 2 after new hiring:",emp1)


# 2.clear():

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

# 3.Pop
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

# 4.popitem():
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

# 5.del()
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)


info = {122:56,'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)




























































