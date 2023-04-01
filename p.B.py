for i in range(0,7):
    for j in range(0,5):
        if((j==0 or j==4)and(i>=0 and i<7)) or ((j==1 or j==2 or j==3) and(i==0 or i==3 or i==6)):
            print("*",end="")
        else:
            print(end=" ")
    print()            