def lcm(x,y):
    if(x>y):
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
     if((x%i==0)and(y%i==0)):
        hcf=i
    return hcf
x=int(input("enter the 1st no"))
y=int(input("enter the 2nd no"))
c=hcf(x,y)
d=x*y/c
print('the lcm of the no.is',d)
