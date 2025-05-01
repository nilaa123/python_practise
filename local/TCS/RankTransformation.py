''' Given array ogf integers , replace each element with its rank 
the rank is its pos in sorted unique values starting from 1
i/p:1 5 8 15 8 25 9
o/p:1 2 3 5 3 6 4'''

arr=list(map(int,input().split(" ")))
unique=sorted(set(arr))
dict={}
rank=1
for i in unique:
    dict[i]=rank
    rank+=1
new=[]
for i in arr:
    print(dict[i],end=' ')
