'''n=int(input("enter the number"))
if(n%2 != 0)or(range(6,20)and(n%2==0)):
    print(" Weird")
else:
    (range(2,6)or(n>20))and(n%2==0)
     print(" not Weired")'''
n=int(input("enter the number"))
if((n%2 != 0)or n%2==0 and n>=6 and n<=20):
    print("Weird")
else:
    print("Not Weired")
