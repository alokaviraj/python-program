n=int(input("enter three digit number"))
R=0
rem=0
rem=n%10
R=R*10+rem
n=int(n/10)      #int for quotient value
rem=n%10          #// also for quotient value
R=R*10+rem
n=int(n/10)
R=R*10+n
print(R)
      
      
      
      
