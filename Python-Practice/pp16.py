#PP16 - Password Generator
from random import randint
import random 
import string

def password():
    uppercase=string.ascii_uppercase
    print(random.choice(uppercase))
    lowercase=string.ascii_lowercase
    print(random.choice(lowercase))
    num=randint(0,9)
    print(str(num))
    symbol=string.punctuation
    print(random.choice(symbol))
    
password()
password()

