"""print even times repeated element
i/p:[1,2,3,2,3,3,4,4,4,4]
o/p:2 4"""


list1=list(map(int,input().strip('[]').split(',')))
d=0
dic={k:d for k in list1}
for i in list1:
    dic[i]+=1
result=""
for i in dic:
    if dic[i]%2==0:
        result=result+" "+str(i)
print(result.strip())
