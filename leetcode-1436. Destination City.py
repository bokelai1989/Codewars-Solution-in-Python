class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        first_city_in_list = []
        for x in paths: # use for loop to go through each element in the list 
            first_city_in_list.append(x[0])
            
        for y in paths:
            if y[1] not in first_city_in_list:
                return y[1] 
