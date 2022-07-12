#PP13- Fibonacci 
def fibo():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        list = []
    elif count == 1:
        list = [1]
    elif count == 2:
        list = [1,1]
    elif count > 2:
        list= [1,1]
        while i < (count - 1):
            list.append(list[i] + list[i-1])
            i += 1

    return list

fibo()