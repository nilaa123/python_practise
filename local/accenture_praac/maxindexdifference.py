def maxindexdifference(arr):
    res=[]
    for k in range(0,len(arr)):
        for j in range(len(arr)-1,-1,-1):
            if(j>k and arr[j]>arr[k]):
                res.append(j-k)
    return max(res)

arr=(int(x) for x in input().split())
arr=list(arr)
print(maxindexdifference(arr))


