weight=int(input("enter ur weight:"))
type=input("(L)bs or (k)g")
if type.upper()=="L":
    new=weight*0.45
    print(f"you weigh {new} in Kgs")
elif type.upper()=='K':
    new=weight/0.45
    print(f"you weigh {new} in Lbs")
else:
    print("enter the unit properly either l or k")