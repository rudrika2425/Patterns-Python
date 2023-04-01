for i in range(0,6):
    for j in range(0,5):
        if((i==0 or i==5)and (j>=0 and j<5))or((i>=0 and i<6)and j==0):
            print("*",end=" ")
        else:
            print(end=" ")
    print()            
                