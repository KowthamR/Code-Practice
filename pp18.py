# PP18- Cows and Bulls
from random import randint 
def game():
    digit1=randint(0,9)
    digit2=randint(0,9)
    digit3=randint(0,9)
    digit4=randint(0,9)
    str_digit1=str(digit1)
    str_digit2=str(digit2)
    str_digit3=str(digit3)
    str_digit4=str(digit4)
    print(str_digit1+str_digit2+str_digit3+str_digit4)
    userguess=(input('Please Enter 4 Numbers'))
    if userguess[0]==str_digit1:
        print('Cow')
    if userguess[0]!=str_digit1:
        print('Bull')
    if userguess[1]==str_digit2:
        print('Cow')
    if userguess[1]!=str_digit2:
        print('Bull')
    if userguess[2]==str_digit3:
        print('Cow')
    if userguess[2]!=str_digit3:
        print('Bull')
    if userguess[3]==str_digit4:
        print('Cow')
    if userguess[3]!=str_digit4:
        print('Bull')
        


game()