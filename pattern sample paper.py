num=int(input("enter number of rows:"))
for i in range(0,num):
    for j in range(0,num-1-i):
        print(end=" ")
    for j in range(0,(2*i)-1):  
        print("*",end="")
    print()    
      
   