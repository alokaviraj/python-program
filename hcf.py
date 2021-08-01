def hcf(x,y):
    if(x>y):
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if((x%i==0)and(y%i==0)):
            hcf=i
    return hcf
x=int(input('enter the 1st no:'))
y=int(input('enter the 2nd no:'))
print('the hcf of the no is',hcf(x,y))
c=hcf(x,y)
d=x*y/c
print('the lcm of the no.is',d)



  


      

