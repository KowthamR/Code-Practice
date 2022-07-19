# Chapter 8 Exercises
# 8.2 string comparison function
def stringcomp():
   x=str(input('Please enter a word'))
   y=str(input('Please enter a word'))
   z=[]
   for i in x:
      if i in y and i not in z:
         z+=i
         print(len(z))

stringcomp()
