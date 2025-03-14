def Productsmallpair(sum1,arr):
    arr.sort()
    if(len(arr)<2):
        return -1
    if(arr[0]==arr[1]):
        return 0
    return arr[0]*arr[1]


arr=(int(x) for x in input().split())
arr=list(arr)
sum1=sum(arr)
print(sum)
result=Productsmallpair(sum1,arr)
print(result)

