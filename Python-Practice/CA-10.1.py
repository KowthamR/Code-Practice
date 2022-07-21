# Chapter 10 Excercises
# 10.1 Vowel Counter formatted for each vowel

def vowel():
    x=str(input('Please Enter a phrase'))
    x=x.lower()
    a_count=x.count('a')
    e_count=x.count('e')
    i_count=x.count('i')
    o_count=x.count('o')
    u_count=x.count('u')

    print('There are {}= a, {}= e, {}= i, {}= o, {}= u, in the phrase'.format(a_count,e_count,i_count,o_count,u_count))
vowel()