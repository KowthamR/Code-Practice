# Gries Chapter 9
# 9.4  Nested List to Unnested
#  Atomic Number/Weight   Be        Mg           Ca          Sr         Ba          Ra
alkaline_earth_metals=[[4,9.012],[12,24.305],[20,40.078],[38,87.62],[56,137.327],[88,226]]
# Printing the atomic number and weight on seperate lines
for i in alkaline_earth_metals:
    print(i[0])
    print(i[1])

# new empty list
number_weight=[]
for i in alkaline_earth_metals:
    number_weight.append(i[0])
    number_weight.append(i[1])
# print new unnested list
print(number_weight)
    
