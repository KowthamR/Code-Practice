# Chapter 4 Exercises
# 4.3 Money Mininumn coins needed
amount=float(input('How much money do you have?'))

def coin():
    dollars,cents=divmod(amount,1)
    print('You have this many dollars: '+ str(dollars))
    total_cents=cents*100
    quarters=total_cents//25
    total_cents-=(quarters*25)
    dimes=total_cents//10
    total_cents-=(dimes*10)
    nickels=total_cents//5
    total_cents-=(nickels*5)
    pennies=round(total_cents/1)
    print('You have this many quarters: '+ str(quarters))
    print('You have this many dimes: '+ str(dimes))
    print('You have this many nickels: '+ str(nickels))
    print('You have this many pennies: '+ str(pennies))
coin()