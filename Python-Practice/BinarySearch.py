# Binary Search
# only works if sorted list
def binary_search(L,x):
    """ Binary Search returns position index of target

    >>> binary_search([1,2,3,4,5,6],2)
    1
    """
    begin_index=0
    end_index=len(L)-1

    while begin_index<=end_index:
        midpoint=begin_index+(end_index-begin_index)//2
        midpoint_value=L[midpoint]
        if midpoint_value==x:
            return midpoint
        elif x<midpoint_value:
            end_index=midpoint-1
        else:
            begin_index=midpoint+1
    return None

binary_search([1,2,3,4,5,6],3)