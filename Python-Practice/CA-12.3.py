# Chapter 12 Excercises
# 12.3 FIFO

queue=[]
while True:
    x=str(input('enter a input'))
    if x=="":
        break
    if x!="?":
        queue.append(x)
    elif len(queue)>0:
        print(queue.pop(0))
    else:
        print('nothing in queue')