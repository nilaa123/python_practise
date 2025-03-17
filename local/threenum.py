a,b,c=map(int,input().split(" "))
i=0
while a!=b and b!=c:
    a+=1
    c-=1
    i+=1
if a==c:
    print(i)
else:
    print(-1)