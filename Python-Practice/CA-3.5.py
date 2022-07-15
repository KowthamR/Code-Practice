# Chapter 3 Exercises
# 3.5  Clock
currenttime=14.00   # 24 hour time
# find hour after 535 hours have passed

def currenthour(x):
    time=(currenttime+x)%24
    print(time)
    
currenthour(535)