# PP6 - String Lists
word=str(input('Please Enter a word'))
print('Your word is:'+ word)
reverseword=word[::-1]
print(reverseword)
if word==reverseword:
    print('Your word is a palindrome')
else:
    print('Your word is not a palindrome')