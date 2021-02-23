# original order 
def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return 'Pls go away and stop eating my sheep'
    else: 
        
        return 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(len(queue) - queue.index("wolf")-1 )

    
# reversed order     
def warn_the_sheep(queue):    
    queue.reverse()
    wolfnum = queue.index("wolf")
    if wolfnum == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number {0}! You are about to be eaten by a wolf!".format(wolfnum)
