import convertors
from convertors import lbs2kg

weight=int(input("enter weight in lbs:"))
new_weight=lbs2kg(weight)
print(new_weight)