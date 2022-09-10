# Gries Chapter 11
# 11.10  d1.keys() == d2.keys()

def db_consistent(D):
    """ (dict)->bool
    Returns True only if the keys of the inner dictionary are the same for every outer dictionary element
    
    >>> db_consistent({'A':{'a':1,'b':2,'c':3}, 'B':{'a':1,'b':2,'c':3}})
    True
    """
    
    for element in D:
        if element.keys()== element.keys():
            return True
        else:
            return False
db_consistent({'A':{'a':1,'b':2,'c':3}, 'B':{'a':1,'b':2,'c':3}})