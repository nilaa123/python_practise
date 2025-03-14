def numberofcarry(num1,num2):
    carry=0
    carry_counter=0
    while num1>0 or num2>0:
        digit1=num1%10
        digit2=num2%10
        total=digit1+digit2+carry
        if total>9:
            carry_counter+=1
            carry=1
        else:
            carry=0
        num1//=10
        num2//=10
    return carry_counter

a=int(input())
b=int(input())
print(numberofcarry(a,b))