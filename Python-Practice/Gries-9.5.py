# Gries Chapter 9
# 9.5 Mystery Function

def mystery_function(vaule):
    """(list)->(list)
    return the sublist reversed but not the outer list

    >>> mystery_function([[1,2,3][4,5,6][7,8,9]])
    [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    """
    result=[]
    for sublist in vaule:
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0,i)
    return result
    
mystery_function([[1,2,3],[4,5,6],[7,8,9]])

# lst=[[1,2,3],[4,5,6],[7,8,9]]
# rev=[i[::-1] for i in lst]     Reverse SUBLIST for element in list
# print(rev)