# Chapter 9 Excercises
# 9.4 Euclids algorthim
# largest common divider berween 2 numbers
def euclid():
    x=int(input('Enter 1st Number'))
    y=int(input('Enter 2nd Number'))
    r=x%y
    while r:
        x=y
        y=r
        r=x%y
    print(str(y))
euclid()
