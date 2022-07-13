# PP24 -GameBoard
def horizontal():
    print('---'*x)

def vertical():
    print('|   '*(x))

x=int(input('How big should the game board be?'))

for i in range(x):
    horizontal()
    vertical()