'''Airport security officials have confiscated several item of the passengers at the security check point.
All the items have been dumped into a huge box (array). Each item possesses a certain amount of risk[0,1,2].
Here, the risk severity of the items represent an array[] of N number of integer values. 
The task here is to sort the items based on their levels of risk in the array. The risk values range from 0 to 2.
Example :

Input :

7  -> Value of N

[1,0,2,0,1,0,2]-> Element of arr[0] to arr[N-1], while input each element is separated by new line.

Output :

0 0 0 1 1 2 2  -> Element after sorting based on risk severity '''

N=int(input())
arr=list(map(int,input().strip('[]').split(',')))
low,mid,high=0,0,N-1
while mid<=high:
    if arr[mid]==0:
        arr[low],arr[mid]=arr[mid],arr[low]
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid+=1
    else:
        arr[high],arr[mid]=arr[mid],arr[high]
        high-=1
print(arr)

'''Time complexity:O(N)
Space complexity:O(1)'''