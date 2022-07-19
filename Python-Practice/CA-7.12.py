# Chapter 7 Exercises
# 7.12 Integer Squares 0 to 100

def integersquares():
    from math import sqrt
    for z in range(0,100):
        for x in range(1,int(sqrt(z))+1):
            for y in range(x,int(sqrt(z))+1):
                if x*x+y*y==z:
                    print('{}={}^2+{}^2'.format(z,x,y))
integersquares()
