def factorial(n):
    fact=1
    if n==1:
        return 1
    else:
        fact=n*factorial(n-1)    
    return fact
print(factorial(5))