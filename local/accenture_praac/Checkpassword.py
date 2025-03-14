def Checkpassword (str):
    if(len(str)<4):
        return 0
    if not any(char.isdigit() for char in str):
        return 0
    if not any(char.isupper() for char in str):
        return 0
    if " " in str or '/' in str:
        return 0
    if (str[0].isdigit()):
        return 0
    return 1
    

str="aA1_67"
print(Checkpassword(str))