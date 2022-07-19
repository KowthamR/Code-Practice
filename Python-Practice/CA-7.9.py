# Chapter 7 Exercises
# 7.9 Computer Guesses our number
number=int(input('Please state a number between 0 and 100'))
def guess():
    from random import randint
    x=randint(0,100)
    while x!=number:
        userinput=input(str(x) + '  H or L')
        if userinput=='H':
            x=randint(0,x) 
        elif userinput=='L':
            x=randint(x,100)
        if x==number:
            print(str(x) + '  I got it')
            break
guess()
