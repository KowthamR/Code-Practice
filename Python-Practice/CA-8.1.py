# Chapter 8 Exercises
# 8.1 multiplication table function
def table():
    x=int(input('Please Enter a Number'))
    for i in range(11):
        print(str(i)+ 'x' +str(x)+'='+str(i*x))
table()