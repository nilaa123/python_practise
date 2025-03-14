#method 1 without creating new list
numbers=[1,2,3,4,3,4,5,6,5,2,1,2]
for item in numbers:
    count=numbers.count(item)
    while count>1:
        numbers.remove(item)
        count-=1
print(numbers)

#method 2 
unique=[]
for item in numbers:
    if(item not in unique):
        unique.append(item)
print(unique)