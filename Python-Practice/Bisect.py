# Bisect
# import bisect
import bisect

def bin_sort(L):
    """ Return a sorted list samllest to largest
    """
    lst=[]
    for i in L:
        bisect.insort_left(lst,i)
    return lst

bin_sort([1,34,6446,86,343,-232,54,343])