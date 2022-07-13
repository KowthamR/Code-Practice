# PP28- max of three variables
def maxofthree(a,b,c):
        if a>b:
                if a>c:
                    print(a)
        if b>a:
                if b>c:
                        print(b)
        if c>a:
                if c>b:
                        print(c)

a=int(input('Enter the 1st number'))
b=int(input('Enter the 2nd number'))
c=int(input('Enter the 3rd number'))
maxofthree(a,b,c) 