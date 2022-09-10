# Gries Chapter 11
# 11.5

def rare_particle(D):
    """ (dict)->(str)
    Takes a dictionary and return the string of the particle least likey to be observed
    
    >>> rare_particle({'neutron':0.55, 'proton': 0.21, 'meson':0.03, 'muon':0.07, 'neutrino':0.14})
    'meson'
    """
    lowest_probablity=min(D, key=D.get)
    print(lowest_probablity)
    
rare_particle({'neutron':0.55, 'proton': 0.21, 'meson':0.03, 'muon':0.07, 'neutrino':0.14})