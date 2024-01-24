
x= int(input("Enter the value of x:"))

match x:
    case 0:
        print("Case is 0")
        
    case 4:
        print("Case is 4")
            
    case _ if(x==99):
        print("X is not above 100")
        
    case _:
      print(x)
