# Chapter 6 Exercises
# 6.3 vowels in a string
def vowel():
    x=str(input('Please enter a sentence'))
    v=0
    if 'a' in x or 'A' in x:
        v+=1
    if 'e' in x or 'E' in x:
        v+=1
    if 'i' in x or 'I' in x:
        v+=1
    if 'o' in x or 'O' in x:
        v+=1
    if 'u' in x or 'U' in x:
        v+=1
    if v==0:
        print('No Vowels')
    elif v==1:
        print('1 Vowel')
    else:
        print('There are '+str(v)+' vowels')

vowel()
