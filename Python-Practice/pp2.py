# PP2- ODD OR EVEN 
# ask for input number
number=input('Please Enter a Number')
print('Your number is:'+number)
# check if even or odd
int_number=int(number)
if int_number%4==0:
     print('Congrats Your number is a multiple of 4')
elif int_number%2==0: 
    print('Your number is even')
else:
     print('Your number is odd')
# extra num/check if equal
num=input('Please Enter your first number')
check=input('Please Enter your 2nd number')
int_num=int(num)
int_check=int(check)
# check if num is divislbe by check
if int_num%int_check==0:
    print('Your 2nd number is evenly divides the first')
else:
    print('Your numbers chosen arent evenly divisble')
    