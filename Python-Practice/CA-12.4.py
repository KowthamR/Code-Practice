# Chapter 12 Excercises
# 12.4 letter counter

def letter(str):
    dict={}
    for i in str:
        keys=dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i]=1
    return dict
letter('cat')
# OR
from collections import Counter
counts=Counter('word')
print(counts)