# Gries Chapter 11
# 11.1

def find_dups(L):
    """ Takes a list of integers returns a set of all duplicate integers

    >>> find_dups([2,3,4,5,2,4])
    {2,4}
    >>> find_dups([1,2,3,4,5])
    { }
    """
    dups=[]
    seen=set()

    for i in L:
        if i in seen:
            dups.append(i)
        else:
            seen.add(i)
    print(dups)

    
find_dups([1,2,3,4,5])