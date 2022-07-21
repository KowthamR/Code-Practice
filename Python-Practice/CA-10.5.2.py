# Chapter 10 Excercises
# 10.5.2 String to ASCII but in order

def code():
    x=str(input('Please Enter a Phrase')) 
    lst=[]
    for i in x:
        lst.append(ord(i))
        lst.sort()
    print(lst)
code()