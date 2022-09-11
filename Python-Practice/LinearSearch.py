# Linear Search 
def linear_search(L,x):
    """ (list)(int)->(int)
    Search list for first occurence of x and return postion
    """
    for i in range(len(L)):
        if L[i]==x:
            print(i)
    return -1
linear_search([1,2,3,4,5],4)

def while_linear_search(L,x):
    """ 
    Same with while
    """
    i=0
    while i !=len(L) and L[i] !=x:
        i=i+1
    if i==len(L):
        return -1
    else:
        print(i)

while_linear_search([1,2,3,4,5],5)