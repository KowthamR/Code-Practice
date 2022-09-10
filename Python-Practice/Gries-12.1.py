# Gries Chapter 12
# 12.1  DNA Sequnce Complement
# DNA consists of A,T,G,C
# A-T Switch and C-G Switch

def complement(DNA):
    """ (str)->(str)
    Takes a string of DNA and produces the complement
    
    >>> complement('AATTGCCGT')
    TTAACGGCA
    """
    dic={'A':'T','T':'A','G':'C','C':'G'} #strings can be changed with dictionary easliy 
    com=''
    for i in DNA:
        com= com+dic[i] 
    print(com)

complement('AATTGCCGT')