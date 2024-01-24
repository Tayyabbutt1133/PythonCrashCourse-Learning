

# In Python, string slicing is a technique used to extract a portion (substring) of a string by specifying its start and end indices.

# myname="Tayyeb shahzad"
# namelen=len(myname)
# print("The length of my name is :",namelen)
# #print(myname[0:6])
# print("After editing my name, correct name is:",myname[0:-8])


myname="Tayyeb"
print("From 0 to 3:")
print(myname[0:2])

print("From 0 to -2")
print(myname[0:-2])
# we can write as
print("Same but with different way")
print(myname[0:len(myname)-2])

print("Negative points")
print(myname[-1:-4]) # Actual backend work: total length=6 [6-1:6-4]=> [5:2] that doesnt make any sense 
# opposite way

print("Other Negative way:")
print(myname[-4:-1]) # Backend working: total length=6 [6-4: 6-1]=> [2:5] that makes sense


instructor="HARRY"
print("Instructor name is:")
print(instructor[-4:-2]) #[1:3]








