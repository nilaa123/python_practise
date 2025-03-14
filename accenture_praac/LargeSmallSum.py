def LargeSmallsum(arr):
    even=[]
    odd=[]
    if(len(arr))<=3:
        return 0   
    for i in range(len(arr)):
        if(arr[i]%2==0):
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    sum=even[1]+odd[1]
    return sum


arr = [int(x) for x in input().split()]
print(LargeSmallsum(arr))