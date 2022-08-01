# Chapter 12 Excercises
# 12.6  Tic Tac Toe Game

layout={'1':' ','2':' ','3':' ',
        '4':' ','5':' ','6':' ',
        '7':' ','8':' ','9':' ',}

moves=[]

for key in layout:
    moves.append(key)


def board(layout):
     print(layout['1'] + '|' + layout['2'] + '|' + layout['3'])
     print('-+-+-')
     print(layout['4'] + '|' + layout['5'] + '|' + layout['6'])
     print('-+-+-')
     print(layout['7'] + '|' + layout['8'] + '|' + layout['9'])

def tictactoe():
    turn='X'
    count=0

    for i in range(10):
        board(layout)
        print('Its your turn '+ turn + ' move where?')

        y=input()

        if layout[y]==' ':
            layout[y]=turn
            count+=1
        else:
            print('Spot already taken')
            continue
        
        if count>=5:
            # top win
            if layout['1'] == layout['2'] == layout['3']!=' ':
                board(layout)
                print('GAME OVER '+ turn +' Won')
                break
            # middle win
            elif layout['4'] == layout['5'] == layout['6']!=' ':
                board(layout)
                print('GAME OVER '+ turn +' Won')
                break
            # bottom win
            elif layout['7'] == layout['8'] == layout['9']!=' ':
                board(layout)
                print('GAME OVER '+ turn +' Won')
                break
            # left side win
            elif layout['1'] == layout['4'] == layout['7']!=' ':
                board(layout)
                print('GAME OVER '+ turn +' Won')
                break
            # down middle win
            elif layout['2'] == layout['5'] == layout['8']!=' ':
                board(layout)
                print('GAME OVER '+ turn +' Won')
                break
            # right sdie win
            elif layout['3'] == layout['6'] == layout['9']!=' ':
                board(layout)
                print('GAME OVER '+ turn +' Won')
                break
            # diagonal wins
            elif layout['1'] == layout['5'] == layout['9']!=' ':
                board(layout)
                print('GAME OVER '+ turn +' Won')
                break
            elif layout['7'] == layout['5'] == layout['3']!=' ':
                board(layout)
                print('GAME OVER '+ turn +' Won')
                break
        # tie situation
        if count==9:
            print('GAME OVER TIE')
        
        if turn=='X':
            turn='O'
        else:
            turn='X'
    again=input('PLAY AGAIN(Y/N)?')
    if again=='y' or again=='Y':
        for key in moves:
            layout[key]=' '
if __name__ == "__main__":
    tictactoe()
       