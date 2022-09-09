# Gries Chapter 8
# 8.7

def same_first_last(L):
    ''' (list) -> bool
    precondition len(L)>=2
    Return True only if first and last item of list are the same
    
    >>> same_first_last([3,4,2,8,3])
    True
    >>> same_first_last(['apple','banana','pear'])
    False
    >>> same_first_last([4.0,4.5])
    False
    '''
    if len(L)<2:
        print('List needs to be longer than 1 item')
    elif L[0]==L[-1]:
        return True
    else:
        return False

same_first_last([3,4,5,6,3])