# Chapter 7 Exercises
# 7.11 Multiplication table

def table():
    number=int(input('Please enter a number: '))
    for row in range(1,number+1):
        print(*("{:3}".format(row*col) for col in range(1, number+1)))
    
   
table()