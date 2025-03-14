def OperationsBinarystring(str):
    str=str.replace("I","1")
    str=str.replace("O","0")
    result=int(str[0])
    for i in range(1,len(str)):
        if (i%2!=0):
            if(str[i]=='C'):
                result=result ^ int(str[i+1])
            if(str[i]=='A'):
                result=result and int(str[i+1])
            if(str[i]=='B'):
                result=result or int(str[i+1])
    return result

str="ICOCICIAOBI"
print(OperationsBinarystring(str))