# Chapter 5 Exercises
# 5.2 Pythagorean Therom
import math
side1=int(input('Length of side 1?'))
side2=int(input('Length of side 2?'))

def pytha():
    side3=math.sqrt(side1**2+side2**2)
    print('The length of side 3 of the triangle is: '+str(round(side3,2)))
    if side1<=0 or side2<=0:
        return('Error please enter a positive number')
pytha()