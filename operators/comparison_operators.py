name=input("enter your name:")

if len(name)<=3:
    print("the name should be longer than 3")
elif len(name)>=50:
    print("the name should be shorter than 50")
else:
    print("name looks fine")

