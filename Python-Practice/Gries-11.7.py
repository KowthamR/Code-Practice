# Gries Chapter 11
# 11.7 Balanced Color RGB
#RGB Total of 1.0 is considered balanced

def is_balanced(D):
    """ dict(str,float)->bool
    Takes a dictionary of R,G,B values if the values add up to 1.0 returns True
    
    >>> is_balanced({'R':0.75, 'B':0.15, 'G':0.10})
    True
    >>> is_balanced({'R':0.75, 'B':0.15, 'G':0.15})
    False
    """
    if sum(D.values())==1.0:
        return True
    else:
        return False
is_balanced({'R':0.75, 'B':0.15, 'G':0.10})