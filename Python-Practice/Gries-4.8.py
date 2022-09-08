# Gries Chapter 4
# 4.8 repeating string function

def repeat(s,n):
    if n<=0:
        return(str(''))
    print(str(s)*n)
repeat('dog',5)