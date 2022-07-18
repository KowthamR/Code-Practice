# Chapter 6 Exercises
# 6.4 Quadratic solutions counter
# -b +- sqrt(b^2-4ac)/2a

def quad():
    from math import sqrt
    a=float(input('Enter A vaule'))
    b=float(input('Enter B vaule'))
    c=float(input('Enter C vaule'))

    if a==0 and b==0:
        print('No unknowns')
    if a==0:
        print('1 solution'+str(-c/b))
    if b**2-4*a*c<0:
        print('No solution')
    if b**2-4*a*c==0:
        print('1 solution')

    sol1=(-b+sqrt((b**2)-(4*a*c)))/(2*a)
    print(sol1)

    sol2=(-b-sqrt((b**2)-(4*a*c)))/(2*a)
    print(sol2)
  
quad()
