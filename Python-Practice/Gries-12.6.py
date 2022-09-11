# Gries Chapter 12
# 12.6 Dutch National Flag

def dutch_flag(L):
    """ (list(str))-> (list(str))
    given a list of strings of colors return a rearranged list with red,green,blue order

    >>> dutch_flag(['red','green','blue','red','green','blue'])
    (['red','red','green','green','blue','blue'])
    """
    # red list
    red=[]
    #green list
    green=[]
    #blue list
    blue=[]

    for i in L:
        if i=='red':
            red.append(i)
        if i=='green':
            green.append(i)
        if i=='blue':
            blue.append(i)
    print(red+green+blue)

dutch_flag(['red','green','blue','red','green','blue','red'])