# Chapter 8 Exercises
# 8.3 Grerory-Leibnitz pi approx.
# gl aprrox = 4 ∗ (1/1 − 1/3 + 1/5 −1/7 + 1/9...)

def gl(n):
    g=0
    for i in range(n):
        if i%2==0:
            g+=1/(1+i*2)
        else:
            g-=1/(1+i*2)
    return 4*g

gl(100)