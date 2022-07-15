# Chapter 3 Exercises
# 3.1 function for wholesale book prices
coverprice=24.95
bookstore_discount=0.60
ship_cost1=3.0
ship_costx=0.75

def wholesale(x):
    wholesaleprice=(coverprice*bookstore_discount*x)+ship_cost1+(ship_costx*(x-1))
    return wholesaleprice

print(round(wholesale(60),2))