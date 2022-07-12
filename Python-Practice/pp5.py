# PP5- List Overlap
a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newlist=[]
for i in a:
    if i in b:
        newlist.append(i)
print(newlist)
# 2nd method
A=set(a)
B=set(b)
C=list(A & B) 
print(C)
