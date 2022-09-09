# Gries Chapter 5 
# 5.11 
age=int(input('Enter your age'))
bmi=float(input('Enter your BMI'))
# definition of young and heavy
young=age<45
heavy=bmi>22.0

if young and not heavy:
    print('low risk')
elif young and heavy:
    print('medium risk')
elif not young and not heavy:
    print('medium risk')
elif not young and heavy:
    print('high risk')
