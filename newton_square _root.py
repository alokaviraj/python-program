def newton_sqrt(n):
    approx=0.5*n
    exact_approx=(0.5*(approx+(n/approx)))
    while(exact_approx!=approx):
                approx=exact_approx
                exact_approx=(0.5*(approx+(n/approx)))
    return approx
n=int(input('enter the number'))
print("the square root by newton method ",newton_sqrt(n))                                   
                                          
