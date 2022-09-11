# Sentinel Search

def sen_search(L,x):
    """ Sentinel Search
    """
    L.append(x)
    i=0

    while L[i]!= x:
        i=i+1
    L.pop()
    if i==len(L):
        return-1
    else:
        print(i)
        
sen_search([1,2,3,4,5],4)