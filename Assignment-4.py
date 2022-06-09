n=int(input())
c=0
m=0
for i in range(1,n+1):
    if(n%i==0 ):
        c+=1
if(c==2):
    print("prime")
else:
    print("not prime")
if(n%2==0):
    print("even")
else:
    print("odd")
if(n%5==0):
    print("yes")

if(n>0):
    for i in range(n+1):
        m+=i
    print(m)
