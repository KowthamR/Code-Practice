#PP20- Element Search
def  search(a,x):
        for i in a:
                if i==x:
                        return True
        if i!=x:
                return False

a =[1,3,5,30,42,43,500]
x=int(input('Enter a Number'))

search(a,x)