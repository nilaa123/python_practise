def anagrams(str1,str2):
    str1new=list(str1.replace(" ","").lower())
    str2new=list(str2.replace(" ","").lower())
    str1new.sort()
    str2new.sort()
    return (str1new==str2new)

str1=input()
str2=input()
result=anagrams(str1,str2)
print(result)