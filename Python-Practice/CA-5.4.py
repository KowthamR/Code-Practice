# Chapter 5 Exercises
# 5.4 calculate e to the power of (-1,0,1,2,3) round to 5 decimal places
a=[-1,1,0,2,3]

def e():
    from math import exp
    b=[]
    for i in a:
        c=round(exp(i),5)
        b.append(c)
    for i in b:
        print(i)

e()