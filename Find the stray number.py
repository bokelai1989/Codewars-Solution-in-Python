def stray(arr):
    arr_set = set(arr) 
    arr_set_1_count = arr.count(list(arr_set)[0]) # this is the way to get element out of a list 
    arr_set_2_count = arr.count(list(arr_set)[1]) 
    
    if arr_set_1_count > arr_set_2_count:
        return list(arr_set)[1]
    else:
        return list(arr_set)[0]

    
    
# use count function 
def stray(arr): 
    
    for x in set(arr):  # using set here is more efficient 
        if arr.count(x) == 1:
            return x 
        

        
# test.assert_equals(stray([1, 1, 1, 1, 1, 1, 2]), 2)
# test.assert_equals(stray([2, 3, 2, 2, 2]), 3)
# test.assert_equals(stray([3, 2, 2, 2, 2]), 3)
