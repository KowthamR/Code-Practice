# PP3 - List Less Than Five
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i<=5:
        print(i)
# make new list with lessthan 5 
print([i for i in a if i<=5])
# ask for number
num=input('Please Enter a number')
int_num=int(num)
for i in a:
    if i<int_num:
        print([i for i in a if i<int_num])
        break
