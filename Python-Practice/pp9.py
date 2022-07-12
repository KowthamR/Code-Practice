# PP9- Guessing Game One
def game():
    from random import randint
    x=randint(0,9)
    usernum=int(input('Please guess a number between 0 and 9'))
    if usernum==x:
        print('You Guessed Right!!!')
    if usernum<x:
        print('too low')
    if usernum>x:
        print('too high')
game()
while True:
    playa=str(input('Do you wanna play again y or n?'))
    if playa=='y':
        game()
    elif playa=='n':
        break
    else:
        print('incorrect answer')
        break
# ATTEMPTS COMEBACK