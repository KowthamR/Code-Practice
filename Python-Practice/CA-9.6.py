# Chapter 9 Excercises
# 9.6 The Towers of Hanoi

disc= 3
def hanoi( pole_from , pole_tmp , pole_to , disc ):
    if disc == 1:
        print( "Disc 1 from", pole_from , "to", pole_to )
        return 1
    moves = hanoi( pole_from , pole_to , pole_tmp , disc -1 )
    print( "Disc", disc , "from", pole_from , "to", pole_to )
    moves += 1+hanoi( pole_tmp , pole_from , pole_to , disc -1)
    return moves
moves = hanoi( ' A ' , ' B ' , ' C ' , disc )
print( moves , "moves needed" )