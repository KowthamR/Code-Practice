# Gries Chapter 11
# 11.6

def count_duplicates(D):
    """ (dict)->(int)
    Takes a dictionary and counts the number of duplicate values
    
    >>> count_duplicates({'test1':1, 'test2':1, 'test3':2, 'test4':2})
    2
    >>> count_duplicates{'test1':1, 'test2':1, 'test3':2, 'test4':4})
    1
    """
    seen=set()
    dup=[]
    for i in D.values():
        if i not in seen:
            seen.add(i)
        else:
            dup.append(i)
    print(len(dup))
    
count_duplicates({'test1':1, 'test2':1, 'test3':2, 'test4':2})