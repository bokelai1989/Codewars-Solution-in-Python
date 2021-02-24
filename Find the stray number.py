def stray(arr):
    arr_set = set(arr) 
    arr_set_1_count = arr.count(list(arr_set)[0]) # this is the way to get element out of a list 
    arr_set_2_count = arr.count(list(arr_set)[1]) 
    
    if arr_set_1_count > arr_set_2_count:
        return list(arr_set)[1]
    else:
        return list(arr_set)[0]
