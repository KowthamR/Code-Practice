# Chapter 8 Excercises
# 8.5 

def mul():
    while True:
        x=int(input('Please Enter a 1st Number'))
        y=int(input('Please Enter a 2nd Number'))

        if x==0:
            break
        if y==0:
            break
        if x<0 or x>1000:
            print('Error Number must be between 0 and 1000')
        if y<0 or y>1000:
            print('Error Number must be betweeen 0 and 1000')
        if x%y==0 or y%x==0:
            print('The numbers cannot be dividers')

        print('Multiplication of '+str(x)+ ' and '+ str(y)+' is '+str(x*y))
        break
mul()