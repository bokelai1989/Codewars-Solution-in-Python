def who_is_paying(name):
    #your code here
    if len(name) < 3:
        return [name]
    else: 
        short_name = name[:2]
        result = [name]
        print(short_name)
        result.append(short_name)
        return result
