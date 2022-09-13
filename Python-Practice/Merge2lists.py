# Merge Two Sorted Lists

def mer(L1,L2):
    """ merge 2 'sorted' lists together
    """
    lst=[]
    i=j=0

    while i!=len(L1) and j!=len(L2):
        if L1[i]<=L2[j]:
            lst.append(L1[i])
            i+=1
        else:
            lst.append(L2[j])
            j+=1
    lst.extend(L1[i:])
    lst.extend(L2[j:])
    return lst

mer([1,2,3,4,5,6],[1,2,3,4,5,6])
