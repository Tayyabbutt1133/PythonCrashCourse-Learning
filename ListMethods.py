# List Methods


# Append() 
l=[11,22,31,43,52,16]
print("Original list is:",l)

l.append(11)
print("After adding: ", l)


# sort()
l.sort()
print("After sorting:",l)

# reverse sort
l.sort(reverse=True)
print("After reverse sort:",l)

# reverse= reverse the original list

print (l.index(11))


print(l.count(11))

m=l
m[0]=0
print(m)
print(l)
# there is a huge difference between both of them 
m=l.copy()
m[0]=0
print(m)
print(l)


l.insert(1,988)
print(l)


m1=[11,212,3242,44,22,43,232,42]
l1=[1,2,3]

m1.extend(l1)
print("Extended version of m1 is: ",m1)


a=m1+l1
print("Concatenation : ", a)