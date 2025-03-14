def Replacecharacter(str,c1,c2):
    str=str.replace(c1,'1')
    str=str.replace(c2,c1)
    str=str.replace('1',c2)
    return str


str='apples'
c1='a'
c2='p'
print(Replacecharacter(str,c1,c2))