# Gries Chapter 12
# 12.3 Hopedale average

def hopedale_average(filename):
    """ 
    Average fox pellets from HopeDale data set
    """
    with open(filename, 'r') as hopedale_file:
        hopedale_file.readline()
        a = hopedale_file.readline().strip()
        while a.startswith('#'):
            a = hopedale_file.readline().strip()
            pelts_list = []
            pelts_list.append(int(a))
            for a in hopedale_file:
                pelts_list.append(int(a.strip()))
            return sum(pelts_list) / len(pelts_list)
  
hopedale_average('hopedale.txt')