def dttob(n):
    value=""
    while n>0:
        value=str(n%2)+value
        n=n//2
    return value
print(dttob(20))

