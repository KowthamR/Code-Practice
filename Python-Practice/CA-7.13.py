# Chapter 7 Exercises
# 7.13 5 Die greater than equal to probablity w/large number of trials
# 5,6 sided die
from random import randint
trail=100000
goodroll=0
for i in range(trail):
    lastroll=0
    for j in range(5):
        roll=randint(0,6)
        if roll<lastroll:
            break
        lastroll=roll
    else: goodroll+=1
print('P={}'.format(goodroll/trail))