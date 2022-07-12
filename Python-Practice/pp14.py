#PP14 - List remove duplicates
def function(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

#this one uses sets
def function2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print(a)
print(function(a))
print(function2(a))
