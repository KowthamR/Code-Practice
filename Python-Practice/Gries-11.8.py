# Gries Chapter 11
# 11.8 

def dict_intersect(D1,D2):
    """ (dict,dict)->(dict)
    Takes two dicitonarys and return a new dictionary containing key,value pairs found in both dictionarys
    
    >>> dict_intersect({'apple':1, 'orange':2, 'cherry':3},{'apple':1, 'blueberry':4, 'lemon':5})
    {'apple':1}
    """
    D3={}
    for (key,value) in D1.items():
        if key in D2 and value==D2[key]:
            D3[key]=value
    print(D3)

dict_intersect({'apple':1, 'orange':2, 'cherry':3},{'apple':1, 'blueberry':4, 'lemon':5})