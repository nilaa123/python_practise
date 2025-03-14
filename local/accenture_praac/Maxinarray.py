def MaxinArray(arr):
    max=arr[0]
    max_index=0
    for i in range(1,len(arr)):
        if(arr[i]>max):
            max=arr[i]
            max_index=i
    return max,max_index


arr=[int(x) for x in input().split()]
max,max_index=MaxinArray(arr)
print(max,"and",max_index)



