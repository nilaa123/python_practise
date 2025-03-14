def operationchoices(a,b,c):
    if c==1:
        return a+b
    elif c==2:
        return a-b
    elif c==3:
        return a*b
    elif c==4:
        return a/b

a=16
b=20
c=2
print(operationchoices(a,b,c))