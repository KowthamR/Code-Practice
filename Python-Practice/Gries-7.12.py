# Gries Chapter 7
# 7.12

def total_occurences(s1,s2,ch):
    """(str,str,str)-int
    precondition: len(ch)==1
    return total number of times ch appears in both s1 and s2
    >>> total_occurences('color','yellow','l')
    3
    >>> total_occurences('blue','red','l')
    0
    """
    if len(ch)!=1:
        print('Error only 1 character')
    counts_s1=s1.count(ch)
    counts_s2=s2.count(ch)
    total=counts_s1+counts_s2
    print(total)

total_occurences('color','yellow','l')