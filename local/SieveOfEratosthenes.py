#Optimal solution to find prime numbers upto N
#Time Complexity-O(N log (log(N)))
#Space Complexity- O(N)
def SOE(N):
    numbers=[True for i in range(N+1)]
    p=2
    while p*p<=N:
        if(numbers[p]==True):
            for i in range(p*p,N+1,p):
                numbers[i]=False
        p+=1
    for i in range(2,N+1):
        if numbers[i]==True:
            print(i)


SOE(10)