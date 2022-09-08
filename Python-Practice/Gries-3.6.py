# Gries Chapter 3
# 3.6 Average Grade Function
from statistics import mean
def grades(a,b,c):
    x=[a,b,c]
    average_grade=mean(x)
    print('The average grade was '+str(average_grade))

grades(65,23,75)