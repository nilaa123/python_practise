def DectoNBase(n,num):
    rem="0123456789ABCDEF"
    result=[]
    q=10
    while(num>0):
        q=num//n
        r=num%n
        result.append(rem[r])
        num=q
    result.reverse()
    result="".join(result)
    return result


n=int(input())
num=int(input())
result=DectoNBase(n,num)
print(result)