# Chapter 11 Excercises
# 11.2 Multiplication of 2 Complex number
# (a*c - b*d) + (a*d + b*c)i

def mulcomplex(c1,c2):
    a=(c1[0]*c2[0])+(c1[0]*c2[1])
    b=(c1[1]*c2[1])+(c1[1]*c2[0])
    print('The two complex numbers multiplied is: {}+{}i'.format(a,b) )
mulcomplex((2,4),(5,6))
