# Gries Chapter 9
# 9.8
# 2 rats weights over 10 days
rat_1=[4,1,3,6,7,1,2,6,9,4]
rat_2=[7,2,6,9,1,8,7,4,2,8]

if rat_1[0]>rat_2[0]:
    print('Rat 1 weighed more than rat 2 on day 1')
else:
    print('Rat 1 weighed less than Rat 2 on day 1')

if rat_1[1]>rat_2[1]:
    print('Rat 1 remained heavier than Rat 2 ')
else:
    print('Rat 2 became heavier than Rat 1')

if rat_1[0]>rat_2[0]:
    if rat_1[-1]>rat_2[-1]:
        print('Rat 1 remained heavier')
    else:
        print('Rat 2 became heavier')
else:
    print('Rat 2 became heavier')
    