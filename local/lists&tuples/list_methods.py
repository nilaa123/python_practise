#append method
numbers=[1,2,3,4,5]
numbers.append(2) 
print(numbers)

#pop 
numbers.pop() #removes the last element

#index
print(numbers.index(4)) # prints the element '4' 's index
# print(numbers.index(15)) #gives error as 15 doesn't exist ,instead use this:-
print(15 in numbers) #gives boolean answer

#insert method (this takes two arguements)
numbers.insert(1,11) #(position,item)
print(numbers)

#remove
numbers.remove(11) #(item) not position
print(numbers)

#count
numbers.append(5)
print(numbers.count(5)) #(item)

#copy
numbers2=numbers.copy()
print(numbers2)

#extend (it is same like append but adds a whole list/tuple or multiple items)
numbers.extend([1,2,3,4,5]) # adding multiple elements
print(numbers)
numbers.extend([[1,2,3,4,5]]) # adding a list to it
print(numbers)