
##PROGRAM:~
##PROGRAM: 
##CODE:
##output :
n=int(input("enter the no"))
temp=n
rev=0
while(n>0):
 rem=n%10
 rev=rev*10+rem
 n=n//10
if(rev==temp):
  print("input is palindrome")
else:
  print("input is not palidrome")

