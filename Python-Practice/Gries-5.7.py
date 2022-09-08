# Gries Chapter 5
# 5.7 

def fx(population,land_area):
    if population<10000000:
        print(population)
    if population>=10000000 and population<=35000000:
        print(population)
    if population/land_area>100:
        print('Densely Populated')
    if population/land_area<100:
        print('Sparsely Populated')
fx(10000,500)
