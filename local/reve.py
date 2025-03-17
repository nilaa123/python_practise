def reverse(array):
    for i in range(0,int(len(array)/2)):
        array[i],array[len(array)-1-i]=array[len(array)-1-i],array[i]
    return array

print(reverse(['a','b','c']))