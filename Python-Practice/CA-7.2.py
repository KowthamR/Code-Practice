# Chapter 7 Exercises
# 7.2 multiplication table w/ while

def table():
    x=int(input('Please Enter a Number'))
    i=0
    while i<11:
        print(str(i)+'x'+str(x)+'='+str(i*x))
        i+=1
table()