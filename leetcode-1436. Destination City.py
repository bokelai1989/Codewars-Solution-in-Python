# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

# Example 1:

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
        

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        first_city_in_list = []
        for x in paths: # use for loop to go through each element in the list 
            first_city_in_list.append(x[0])
            
        for y in paths:
            if y[1] not in first_city_in_list:
                return y[1] 
