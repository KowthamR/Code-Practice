# Selection Sort 

# find_min function
def find_min(L,b):
    """ (list,int)-> int
    Return the index of the smallest vaule in L
    """
    smallest=b # the index o the samllest so far
    i=b+1
    while i!=len(L):
        if L[i]<L[smallest]:
            smallest=i
        i=i+1
    return smallest
find_min([3,-1,7,5],2)

# selection_sort function
def selection_sort(L):
    """ Reorders items in a list from smallest to largeest
    """
    i=0
    while i!=len(L):
        smallest=find_min(L,i)          # Using find_min function
        (L[i],L[smallest])=(L[smallest],L[i])
        i=i+1
    print(L)
selection_sort([3,-1,7,5])