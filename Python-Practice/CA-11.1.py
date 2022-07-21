# Chapter 11 Excercises
# 11.1 Addition between 2 complex numbers
# complex number of the form a+b(i)   i=sqrt(-1)

def addcomplex(c1,c2):
    a=c1[0]+c2[0]
    b=c1[1]+c2[1]
    print('The two complex numbers added is: {}+{}i'.format(a,b))
   

addcomplex((2,9),(5,3))
    