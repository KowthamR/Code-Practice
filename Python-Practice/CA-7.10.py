# Chapter 7 Exercises
# 7.10 Prime number check

def prime(n):
    num=int(input('Please Enter a number'))
    a=[ i for i in range(2,num) if num%i==0]
    if num>1:
        if len(a)==0:
            print('Prime')
        else:
            print('Not Prime')
    else:
        print('Not Prime')
prime(5)