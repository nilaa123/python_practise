"""names=['heather','harry','sara','ron']
print(names[1:])#no replacing here
names[0]='winter'#here it is permantely replaced
print(f'{names[0]} is new here')
print(names)"""

num=[12,23,11,34,2]
highest=num[0]
for i in num:
    if highest<i:
        highest=i
print(highest)