# Chapter 7 Exercises
# 7.5 Fibonacci

def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibo(n-1)+fibo(n-2)

fibo(3)