# Gries Chapter 11
# 11.2 Gerbils
# Gerbil mating pair 
def mating_pairs(males,females):
    """ (set)(set)->(tuple)
    takes two sets 1 male and 1 female returns pairs of tuples consisting of 1 male and 1 female
    
    >>> mating_pairs({1,2,3,4,5},{6,7,8,9,10})
    (1,6) (2,7) (3,8) (4,9) (5,10)
    >>> mating_pairs({'don','roger','max'},{'kat','ally','eli'})
    ('don','kat') ('roger','ally') ('max','eli')
    """
    if len(males)!=len(females):
        print('error same number of male and females required')
    num_of_gerbils=len(males)
    pair=set()
    for i in range(num_of_gerbils):
        male=males.pop()
        female=females.pop()
        pair.add((male,female),)
    return pair

mating_pairs({'don','roger','max'},{'kat','ally','eli'})