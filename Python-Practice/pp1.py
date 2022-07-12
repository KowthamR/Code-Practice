# PP1- Character Input 
# name input
name=input('Whats your name?')
print('Your name is:'+ name)
# Current year is 2022
current_year=2022
# age input
age=input('Whats your age?')
print('Your age is:'+ age)
# convert str to int
int_age=int(age)
years_to_100=100-int_age
hundred=2022+years_to_100
# convert int to str
str_hundred=str(hundred)
print('The year you turn 100 will be:'+ str_hundred)
# extra input another number between 1 to 10
extra=input('Can you give me another number between 1 and 10?')
int_extra=int(extra)
if int_extra>10 :print('error number too big')
if int_extra<0 :print('error number too small')
str_extra=str(int_extra)
# printing message new number of times
print('Your new number is:'+ str_extra)
for number in range(int_extra):
    print('The year you turn 100 will be:'+ str_hundred)






