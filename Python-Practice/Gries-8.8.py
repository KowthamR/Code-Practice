# Gries Chapter 8
# 8.8

def is_longer(L1,L2):
    """(list,list)->bool
    Return True only if L1 is longer than L2

    >>> is_longer([1,2,3],[4,5])
    True
    >>> is_longer(['abcdef'],['ab','cd','ef'])
    False
    >>> is_longer(['a','b','c'],[1,2,3])
    False
    """
    if len(L1)>len(L2):
        return True
    else:
        return False

is_longer(['a','b','c'],[1,2,3])