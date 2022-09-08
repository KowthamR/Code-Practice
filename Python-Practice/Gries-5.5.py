# Gries Chapter 5
# 5.5 absoulte check function

def check(x):
    if x==abs(x):
        return True
    if x!=abs(x):
        result=abs(x)
        print(result)
        return False
  
        

check(-452)
