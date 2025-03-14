price=int(input("enter the price of the property"))
buyer_goodcredit=(input("Does the buyer have good credit bro -_-  ")).lower()=='true' #enter whether True or False 
salary=int(input("Enter the salary of the Client "))
if buyer_goodcredit:
    print("#")
    initial_price=0.10*price
elif salary >=10000:
    initial_price=0.15*price
else:
    initial_price=0.20*price
print(f'your initial price is {initial_price}')
print("congrats on your new purschase")
