#  smallest so far
from itertools import count
from operator import truediv
from pickle import GET
from tkinter.tix import DirList


smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
# in function repeats for all objects in a list/string
for n in "banana":
    print(n)
# len function returns length 
dog='dog'
print(len(dog))
#  == is equality operator 
cat=4==4.0
print(cat)
# find function locates i=location of item serached for
word = "banana"
i = word.find("na")
# Chapter 7 \n
sentence='The\nduck\nswam\nacross\nthe\nlake'
print(sentence)
# lists [lists]
fruit = "banana"
x = fruit[1]
# word splitting 
words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
# dictionary
days_of_the_week={"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
print(days_of_the_week)
print(days_of_the_week['tuesday'])
# tuple (key,vaule)
d=dict()
d['mark']=55
d['gwen']=66
print(d)
for (k,v) in d.items():
    print (k,v)
# sorting dictionarys
d={'a':10,'b':20,'c':30}
print(d.items())
print(sorted(d.items()))
# switch the key,vaule order in a tuple
new_d=list()
for k,v in d.items():
    new_d.append((v,k))
print(new_d)
# sorted method for flipping key,vaule
print(sorted( [(v,k) for k,v in d.items()]))
# Regular Expressions
import re
quote='monkey madness all around town'
print(re.search('^monkey',quote))
# Matching and Extracting Using RE
favnum='My 2 favourite numbers are 7 and 22'
favnumy=re.findall('[0-9]+',favnum)
print(favnumy)
# Greedy matching 
favnumz=re.findall('^M+y',favnum)
print(favnumz)
# character represent using ord function gives ASCII Character
# 8 bits into a byte
print(ord('H'))
print(ord('e'))
# URLIB function 
import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
# JSON - javascript object notation
# XML- Extensible markup langauge
import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])
# Classes
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()
# A class defines object properties including a valid 
# range of values, and a default value. A class also 
# describes object behavior. An object is a member or an 
# "instance" of a class.
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()
# class- template
# attriubute- variable in a class
# method a function in a class
# object - particular instance of a class
# constructor code that run when object is created
# inhertiance the ability to make new class by extending parent class













