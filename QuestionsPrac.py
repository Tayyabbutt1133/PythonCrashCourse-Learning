# Write a function that takes an integer as input and prints whether it is even or odd.
# Function calling
def evenprint():
   print("Given Number is even")

def oddprint():
    print("Given Number is odd")
# user input
userask=int(input("Enter number to check even or odd: "))
if(userask%2==0):
  evenprint()
 
else:
 oddprint()
 
 
 # Write a function that takes three numbers as input and returns the maximum of the three.

def maxnum(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c



Max1=int(input("Enter First Number: "))
Max2=int (input("Enter Second Number: "))
Max3=int (input("Enter Third Number: "))
maximum=0
maximum=maxnum(Max1,Max2,Max3)
print("Maximum Number is:",maximum)







