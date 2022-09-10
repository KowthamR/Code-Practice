# Gries Chapter 11
# 11.4

def count_vaules(D):
    """ (dic)->(int)
    Takes a dictionary and counts and returns the number of distinct vaules
    
    >>> count_vaules({'red':1, 'green':1, 'blue':2})
    2
    >>> count_vaules({'dog':4, 'cat':5, 'mice':6})
    3
   """
    distinct_vaules=set(D.values())
    num_distinct_vaules=len(distinct_vaules)
    print(num_distinct_vaules)

count_vaules({'red':1, 'green':1, 'blue':2})