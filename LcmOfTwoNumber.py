'''a=int(input("please enter the first value a"))
b=int(input("please Enter the second number"))
i=1
while(i<=a and i<=b):
    if(a%i==0 and b%i==0):
        HCF=i
    i=i+1
print("\n HCf of{0} and {1}={2}".format(a,b,HCF))'''
'''for i in range(1,6):
    x=65
    for j in range(1,i+1):
        print(chr(x),end="")
        x+=1
    print()'''
'''def fib(n):
    if(n<=1):
        return n
    else: 
        return fib(n-1)+fib(n-2)
n=int(input("enter the  no"))
print("fib series")
for i in range(n ):
    print(fib(i))'''
a=int(input("please enter the first value a"))
b=int(input("please Enter the second number"))
number_min=min(a,b)
while(1):
    if(number_min%a==0 and number_min%b==0):
        print("lcm is",number_min)
        break
    number_min=number_min+1





