# Gries Chapter 3
# 3.7 Grades average of three highest 

from statistics import mean
def average_of_top_3(a,b,c,d):
    x=[a,b,c,d]
    x.remove(min(x))
    average_grade=mean(x)
    print('The average of the three highest was '+str(average_grade))

average_of_top_3(25,64,85,35)