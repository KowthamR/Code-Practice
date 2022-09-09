# Gries Chapter 7
# 7.5 
a='avocado'.find('o',2)                  # Gives first index of'o'
b='avocado'.find('o', 'avocado'.find('o') + 1)     # Gives 2nd index of 'o'
print(a,b)