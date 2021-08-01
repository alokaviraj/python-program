n=int(input("enter the number"))
if(n>1):
 for i in range(2,n//2):
         if(n%i==0)and(n%n==0):
            print("number is prime")
 else:
    print("number is not prime")
