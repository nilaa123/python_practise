''' A chocolate factory is packing chocolates into the packets. 
The chocolate packets here represent an array  of N number of integer values. 
The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).
Example 1 :

N=8 and arr = [4,5,0,1,9,0,5,0].

There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array '''

N=int(input())
arr=list(map(int,input().strip("[]").split(",")))
non_empty=0
for i in range(N):
    if arr[i]!=0:
        arr[non_empty]=arr[i]
        non_empty+=1
for i in range(non_empty,N):
    arr[i]=0

print(arr)

'''
time Complexity:O(N)
Space Complecity:O(1)
'''
