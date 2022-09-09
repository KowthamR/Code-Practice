# Gries Chapter 9
# 9.12 
def remove_neg(num_list):
    """ (list)->(list)
    Removes all negative numbers from a list of numbers

    >>> remove_neg(1,-2,-3,4,5,-6,7,8,-9)
    [1,4,5,7,8]
    >>> remove_neg(-5,1,-3,2)
    [1,2]
    """
    i=0
    while i < len(num_list):
        if num_list[i]<0:
            del num_list[i]
        else:
            i+=1
   
    print(num_list)

remove_neg([1,-2,-3,4,5,-6,7,8,-9])