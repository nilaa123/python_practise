def maximum_in_arr(arr):
    maximum=arr[0]
    for i in arr:
        if i>maximum:
            maximum=i
    return maximum