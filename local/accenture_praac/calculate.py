def calculate(m,n):
    sum=0
    for i in range(m,n):
        if(i%3==0 and i%5==0):
            sum+=i
    return sum


m=12
n=50
print(calculate(m,n))