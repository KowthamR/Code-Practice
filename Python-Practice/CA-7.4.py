# Chapter 7 Exercises
# 7.4   99 bottles of beeeer!!!

def beer(i):
   while i>=0:
        print(str(i)+ ' bottles of beer on the wall '+   str(i)+ ' bottles of beer.'  ' take one down, pass it around,'+  str(i)+' bottles of beer on the wall.')
        i-=1
beer(10)