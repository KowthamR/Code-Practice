# Chapter 12 Excercises
# 12.2 Random Playing Card

def cards():
    suite=['Hearts','Spade', 'Clubs','Diamond']
    vaule=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    deck=[]

    for v in vaule:
        for s in suite:
            deck.append(v+' Of '+s)
    import random
    print(random.choice(deck))
cards()
