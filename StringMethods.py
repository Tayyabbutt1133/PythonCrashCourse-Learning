# Strings Methods in Python
# 1.upper()
# 2.lower()
# 3.rstrip()
# 4.len()
# 5.replace()
# 6.Split()
# 7.capitalize()
# 8.center()
# 9.count()
# 10.endswith()
# 11.find() if the finding word is not present it will return -1
# 12.index() if the fidning word is not present in the string it will give error and terminate the program
# 13.isalnum() checking condition for alpanumeric 
# 14.isalpha() checking condition for alphabets
# 15.islower() checking condition
# 16.isprintable() 
# 17.title() istitle()
# 18.swapcase() swap letter from upper to lower and vice versa
# 19.startswith()
# 20.isspace()


#Strings are immutable(Unchanged) in python
ApnaName="tayyeb @@@@@@@@@"
print("Length of Name is:",len(ApnaName))


print("UpperCase:",ApnaName.upper())

print("LowerCase:",ApnaName.lower())


print(ApnaName.rstrip("@"))

print("Replacing name : ",ApnaName.replace("tayyeb","Legend"))


print("Splitting spaces:",ApnaName.split(" "))


checking="Introduction to Python"

print(checking.capitalize())


ending="12Welcometomyspace" # works as total length-1
print(ending.endswith("@")) # Give true/false on the basis of last word that you want to check in a statement

print("Length is:",len(ending))
print("check12:")
print(ending.endswith("to",0,10))  # check given word in between the given distance



print(ending.find("to")) # give the first occurence comes in the string 


print(ending.isalnum())


print(ending.isalpha())

lower="tayyeb"
print(lower.islower())



str1 = "We wish you a Merry Christmas"
print(str1.isprintable())



str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())


str1 = "World Health Organization" 
print(str1.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())


str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())