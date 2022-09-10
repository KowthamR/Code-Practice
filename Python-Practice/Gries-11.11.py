# Gries Chapter 11
# 11.11  Sparse Vectors

def sparse_add(D1,D2):
    """ (dict)(dict)->(dict)
    Adds two Sparse vectors stored as Dictionarys
    
    >>> sparse_add({1:1, 3:1},{0:1, 2:1})
    {1: 1, 3: 1, 0: 1, 2: 1}
    """
    D3=D1.copy()
    for i in D2:
        if i in D3:
            D3[i]=D3[i]+D2[i]
        else:
            D3[i]=D2[i]
    print(D3)
sparse_add({1:1, 3:1},{0:1, 2:1})

def sparse_dot(D1,D2):
    """ (dict)(dict)->(dict)
    Dot Product of two sparse vectors
    
    >>> sparse_dot({1:2, 3:1},{3:2, 2:1})
    2
    """
    D3=0
    for i in D2:
        if i in D1:
            D3=D3+D1[i]*D2[i]
    print(D3)
sparse_dot({1:2, 3:1},{3:2, 2:1})