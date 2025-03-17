def MaxNumRec(array,length):
    if length==1:
        return array[0]
    else:
        return max(array[length-1],MaxNumRec(array,length-1))
    
print(MaxNumRec([1,2,23,4],4))