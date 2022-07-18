# Chapter 7 Exercises
# 7.3  10 numbers smallest/largest/ # divisible by 3

def numbers():
    x=[]
    for i in range(10):
        y=int(input('Please enter 10 numbers'))
        x.append(y)
    smallest=min(x)
    largest=max(x)
    print(smallest)
    print(largest)
    for i in range(0,len(x)):
        if x[i]%3==0:
            print('numbers divisible by 3 are: '+str(x[i]))
  
numbers()