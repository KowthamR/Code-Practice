# Chapter 6 Exercises
# 6.1 Grade returner

def grade():
    x=float(input('Enter the grade number'))
    x=x*2
    x=round(x)/2
    if x<0 or x>10:
        print('Error grade point cannot be less than 0 and greater than 10')
    elif x>=8.5:
            print('A')
    elif x==7.5 or x==8:
        print('B')
    elif x==6.5 or x==7:
        print('C')
    elif x==5.5 or x==6:
        print('D')
    elif x<=5:
        print('F')
grade()
