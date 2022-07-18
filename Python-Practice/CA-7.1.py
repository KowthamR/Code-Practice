# Chapter 7 Exercises
# 7.1 multiplication table

def table():
    x=int(input('Please Enter a Number'))
    for i in range(11):
        print(str(i)+ 'x' +str(x)+'='+str(i*x))
table()