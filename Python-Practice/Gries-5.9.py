# Gries Chapter 5
# 5.9 PH Warning 
# if below 3 print strong warning

def ph(a):
    if a<=3.0:
        print('Warning TOO Acidic')
    if a>3 and a<6:
        print('Acidic')
    if a>=6 and a<=8:
        print('Neutral')
    if a>8 and a<=14:
        print('Basic')

        
ph(11)
