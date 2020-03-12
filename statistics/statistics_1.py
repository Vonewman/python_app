def mysum(mylist):
    """ Compute the um of elements
    Input: a list of numbers
    Output: their sum """
    
    s = 0
    for x in mylist:
        s = s + x
    return s

# Test
print("--- Sum ---")
mylist = [5, 18, 6, 3]
print(mylist)
print(mysum(mylist))
print(sum(mylist))

def mean(mylist):
    """ Compute the average of the items of the list
    Input: a list of numbers
    Output: the average """

    nblist = len(mylist)

    if nblist == 0:
        avg = 0
    else:
        avg = mysum(mylist) / nblist

    return avg

# Test
print("--- Mean ---")
mylist = [5, 18, 6, 3]
print(mylist)
print(mean(mylist))


def minimum(nylist):
    """ Return the minimum among the elements
    Input: a list of numbers
    Output: their maximum """

    if len(mylist) == 0:
        return None

    mini = mylist[0]
    for i in range(1, len(mylist)):
        if mylist[i] < mini:
            mini = mylist[i]

    return mini

# Test
print("--- Minimum ---")
print(minimum(mylist))
print(min(mylist))

def maximum(mylist):
    """ Return the maximum among the elements 
    Input: a list of numbers
    Output: their maximum
    """
    if len(mylist) == 0:
        return None

    maxi = mylist[0]
    for i in range(1, len(mylist)):
        if mylist[i] > maxi:
            maxi = mylist[i]

    return maxi

# Test
print("--- Maximum ---")
mylist = [6,8,2,10]
print(mylist)
print(maximum(mylist))
print(max(mylist))





    
