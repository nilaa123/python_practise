def differenceofSum(n,m):
    sum1,sum2=0,0
    for i in range(1,n+1):
        if(i%m)==0:
            sum1+=i
        else:
            sum2+=i
    result=abs(sum1-sum2)
    return result

n=int(input())
m=int(input())
result=differenceofSum(n,m)
print(result)