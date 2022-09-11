# Gries Chapter 12
# 12.2
from operator import index
def small(L):
    """ 
    Finds smallest in a list
    
    >>> small([1,2,3,4])
    1
    """
    a=min(L)
    b=L.index(min(L))
    print(a,b)

small([6,2,3,4])

def smallorbig(L,bool):
    """ (list)(bool)->(tuple)
    Takes a list and bool and rtuens either the smallest or biggest value with its index
    True-(Min,[Min])
    False-(Max,[Max])
    >>> smallorbig([1,2,3,4],True)
    """
    if bool==True:
        a=min(L)
        b=L.index(min(L))
        tup=(a,b)
        print(tup)
    if bool==False:
        a=max(L)
        b=L.index(max(L))
        tup=(a,b)
        print(tup)

smallorbig([1,2,3,4],False)