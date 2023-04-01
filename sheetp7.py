n=ord("A")
for i in range(1,6):
    for j in range(1,1+i):
        print(chr(n),end=" ")
        n+=1
    print()    