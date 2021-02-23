def is_prime(n):
    # if the number is smaller than 0 or equal to 1, then it is not a Prime number --> False 
    if n<= 0 or n == 1:
        return False
    i = 2
    while (i <= n** 0.5):
        if n % i == 0:
            return False 
        i += 1
    return True 
