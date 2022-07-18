# Chapter 7 Exercises
# 7.6 String comparison

def stringcomp():
   x=str(input('Please enter a word'))
   y=str(input('Please enter a word'))
   z=[]
   for i in x:
      if i in y and i not in z:
         z+=i
         print(z)

stringcomp()