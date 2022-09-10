# Gries Chapter 11
# 11.9   Inner headings in DB

def db_headings(D):
    """ (dict)->(set)
    Returns Headings in the form of a set from an inner dictionary within dictionary
    
    >>> db_headings({'jgoodall':{'surname':'Goodall', 'forename':'Jane', 'born':1934, 'died':'none'}}
    ('surname','forename','born',died')
    """
    headings=set()
    for i in D:
        for heading in D[i]:
            headings.add(heading)
    print(headings)
db_headings({'jgoodall':{'surname':'Goodall', 'forename':'Jane', 'born':1934, 'died':'none'}})