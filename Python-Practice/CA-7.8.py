# Chapter 7 Exercises
# 7.8 Guessing Game 0 to 1000

def game():
    from random import randint
    x=randint(0,1000)
    print(x)
    attempt=0
    guess=int(input('0 to 1000?'))
    while guess!=x:
        if guess<0 or guess>1000:
            attempt+=1
            print('Error')
        if guess<x:
            attempt+=1
            print('Higher')
        elif guess>x:
            attempt+=1
            print('Lower')
        guess=int(input('Try again'))
        if guess==x:
            print('Congrats')
            print('Number of attempts: '+str(attempt))
            break
        
game()