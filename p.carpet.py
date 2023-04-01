for i in range(1,6):
    for j in range(1,16):
        if(i==1 or i==5):
            if(j>=1 and j<7 or j>9 and j<16):
             print("-",end=" ")
            if j==8:
                 print("|",end=" ")
            if j==7 or j==9:
                print("#",end=" ")
            
        if(i==2 or i==4):
             if(j>=1 and j<5) or  (j>12 and j<16):
              print("-",end=" ") 
             if j==5 or j==8 or j==11:
              print("|",end="")  
             if j==4 or j==6 or j==7 or j==8 or j==10:
              print("#",end=" ")
        if(i==3):
            if j<=1 and j>5 or j>11 or j<16:
                print("-",end=" ")     
            if(j==5):
                print("WELCOME",end=" ")     
             
    print()   