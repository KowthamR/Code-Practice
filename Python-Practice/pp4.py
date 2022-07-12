# PP4- Divisors
x=int(input('please enter a number'))
y=list(range(1,x+1,1))
newlist=[]
for i in y:
    if x%i==0:
        newlist.append(i)
print(newlist)