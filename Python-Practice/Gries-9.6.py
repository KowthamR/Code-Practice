# Gries Chapter 9
# 9.6
text=" "
while text.lower()!="quit":
    text=input('Please enter a chemical formula or \'quit\' to exit')
    if text=='quit':
        print('exit')
    elif text=='H2O':
        print('Water')
    elif text=='NH3':
        print('Ammonia')
    elif text=='CH4':
        print('Methane')
    else:
        print('Unknown Compound')