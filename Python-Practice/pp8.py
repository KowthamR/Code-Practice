# PP8- Rock Paper Scissors
player1= str(input('Player please enter rock,paper,scissors'))
player2= str(input('Player please enter rock,paper,scissors'))
def game():
    while player1=='rock':
        if player2=='rock':
         print('The game is a tie')
         break
        elif player2=='paper':
            print(' Congrats Player 2 Wins')
            break
        elif player2=='scissors':
            print('Congrats Player 1 Wins')
            break
    while player1=='paper':
        if player2=='paper':
             print('The game is a tie')
             break
        elif player2=='rock':
             print('Congrats Player 1 Wins ')
             break
        elif player2=='scissors':
             print('Congrats Player 2 Wins')
             break
    while player1=='scissors':
        if player2=='scissors':
            print('The game is a tie')
            break
        elif player2=='rock':
             print('Congrats Player 2 Wins')
             break
        elif player2=='paper':
             print('Congrats Player 1 Wins')
             break
    print('Want to play again yes or no?')
# COME BACK AND FIX
answer=str(input('yes or no'))
while answer=='yes':
    game()
    break


