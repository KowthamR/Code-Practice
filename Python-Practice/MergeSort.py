# Mergesort
from heapq import merge

def mergesort(L):
    """ Reorder from smallest to largest
    """
    # Divide list into left and right halfs
    if len(L)>1:
        midpoint=len(L)//2
        left=L[:midpoint]
        right=L[midpoint:]

        mergesort(left)
        mergesort(right)

        i=j=k=0
# compare left and right and assign lower values first to L (list)
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                L[k]=left[i]
                i+=1
            else:
                L[k]=right[j]
                j+=1
            k+=1
        

        while i<len(left):
            L[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            L[k]=right[j]
            j+=1
            k+=1
    return L

mergesort([3,2323,-2424,446,67675,-424])