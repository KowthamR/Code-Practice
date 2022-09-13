# Insertion Sort 
 
def insert(L,b):
    """ Insert L[b] where it belongs in L[0:b+1]
    note:L[0:b] is already sorted
    """
    i=b
    while i!=0 and L[i-1]>=L[b]:
        i=i-1
    value=L[b]
    del L[b]
    L.insert(i,value)

def insertion_sort(L):
    """ Reorder from smallest to largest
    """
    i=0
    while i!=len(L):
        insert(L,i)     # use insert function
        i=i+1
    print(L)

insertion_sort([2,6,2,7,24,565,2,46,23,78,44])