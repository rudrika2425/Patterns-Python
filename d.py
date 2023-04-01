'''a=int(input())
temp=a
s=0
while(temp>0):
    c=temp%10
    s+=(c**3)
    temp=temp//10
if(s==a):
     print("armstrong") 
else:
    print("not armstrong")'''

from math import factorial
num=int(input())
digits=list(str(num))
total=0
for i in digits:
    total+=factorial(int(i))
if(total==num):
    print("strong")
else:
    print("no strong")
    
num=int(input())
digits=list(str(num))
print(digits)

n=int(input())
n1=0
n2=0
print(n1,n2,end="")
for i in range(3,n+1):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,ends="")
    
    
    
