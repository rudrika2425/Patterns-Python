num=int(input("enter the size of diamond: "))
for i in range(0,num):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for k in range(num-1,0,-1):
    for m in range(0,num-1-k+2):
        print(end=" ")
    for m in range(0,k):
        print("*",end=" ")
    print()            