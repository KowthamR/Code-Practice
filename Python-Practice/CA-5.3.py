# Chapter 5 Exercises
# 5.3  Ask user for 3 number, print largest,smallest and average rounded
def number():
    numbers=[]
    for i in range(3):
        a=int(input('Please enter a number'))
        numbers.append(a)
    print('The largest number is: '+str(max(numbers)))
    print('The smallest number is: '+str(min(numbers)))
    from statistics import mean
    ave=round(mean(numbers),2)
    print('The average between the numbers is: '+str(ave))

number()