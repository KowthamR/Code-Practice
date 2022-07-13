# PP26- Check tic tac toe
def gamechecker(a,b,c,d,e,f,g,h,i):
        # player 1
        # Horizontal wins
        if a==1 and b==1 and c==1:
                return ('player 1 wins')
        if d==1 and e==1 and f==1:
                return('player 1 wins')
        if g==1 and h==1 and i==1:
                return('player 1 wins')
        # Vertical Wins
        if a==1 and d==1 and g==1:
                return('player 1 wins')
        if b==1 and e==1 and h==1:
                return('player 1 wins')
        if c==1 and f==1 and i==1:
                return('player 1 wins')
        # Diagonal wins
        if a==1 and e==1 and i==1:
                return('player 1 wins')
        if c==1 and e==1 and g==1:
                return('player 1 wins')

        # player 2
        # Horizontal wins
        if a==2 and b==2 and c==2:
                return ('player 2 wins')
        if d==2 and e==2 and f==2:
                return('player 2 wins')
        if g==2 and h==2 and i==2:
                return('player 2 wins')
        # Vertical Wins
        if a==2 and d==2 and g==2:
                return('player 2 wins')
        if b==2 and e==2 and h==2:
                return('player 2 wins')
        if c==2 and f==2 and i==2:
                return('player 2 wins')
        # Diagonal wins
        if a==2 and e==2 and i==2:
                return('player 2 wins')
        if c==2 and e==2 and g==2:
                return('player 2 wins')


#gamechecker(a,b,c,d,e,f,g,h,i)
