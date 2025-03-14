#Must leave two lines after a function def for PEP 8
def greet(name,yr): #(paramaters)
    print(f"good morning {name}")
    print(f"You look younger than {yr}")
    print("Did you have breakfast?")


name=input("what's your name:")
yr=input("what's your age:")
greet(name,yr) #(arguements)
