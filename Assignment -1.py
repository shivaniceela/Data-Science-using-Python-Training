ai=int(input())
hra=int(input())
d=int(input())
y=hra*12
t=ai-y-d
if(t<300000):
    print("0")
elif(t<300000 and t>600000):
    print(0.1*t)
elif(t<600000 and t>1000000):
    print(0.15*t)
else:
     print(0.2*t)
