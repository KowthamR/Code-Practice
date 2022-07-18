# Chapter 7 Exercises
# 7.7 approx pi with n-darts thrown

def darts(n):
   from random import random
   from math import sqrt
   c=0
   for i in range(n):
      x=random()
      y=random()
      if sqrt(x**2+y**2)<1:
         c+=1
   print('A approximation of pi is '+str((4*c)/n))

darts(1500)