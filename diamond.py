for i in range(1,6):
    for j in range(1,6-i):
        print(end=" ")
    for j in range(0,2*i):
        print("*",end="")
    print()        
for i in range(5,0,-1):
    for j in range(1,5-i):
        print(end=" ")
    for j in range(0,2*i):
        print("*",end="")
    print() 