import sys
from typing import final
import All_functions
from copy import deepcopy
maximum = sys.maxsize
minimum = -sys.maxsize
s = int(sys.argv[3])
    
def WriteBoard(out_state):
    board2 = open(sys.argv[2],"w")
    for every in out_state:
        board2.write(every)
    board2.close()

def StaticEstimationOpening(static_board):
    count_of_white = 0
    count_of_black = 0
    static_board = deepcopy(static_board)
    for position in range(0, len(static_board)):
        if(static_board[position]== 'W'):
            count_of_white = count_of_white + 1;   #increementing the count of white
        elif(static_board[position]== 'B'):
            count_of_black = count_of_black + 1;   #increementing the count of black
    static_estimate_opening = count_of_white - count_of_black
    return static_estimate_opening 

def ReadBoard():
    board1 = open(sys.argv[1],"r")
    board = []
    for long in board1:
        for character in long:
            board.append(character)
    board1.close()
    return board

def ABOpening(s, game_board, alpha, beta, flag):
    output = All_functions.outputClass()
    input = All_functions.outputClass()
    board_list = []
    if (s == 0):
        final = StaticEstimationOpening(game_board)
        output = All_functions.outputClass(final, output.count + 1, game_board)
        return output

    if (flag == 1):
        board_list = All_functions.GenerateMovesOpening(game_board)
        output.value = minimum

    else:
        board_list = All_functions.generateMoveOpeningBlack(game_board)
        output.value = maximum

    for bposition in board_list:
        if (flag == 1):
            input = ABOpening(s - 1, bposition, alpha, beta, 0)
            if (input.value > alpha):
                alpha = input.value
                output.board_state = bposition
            output.count = output.count + input.count

        else:
            input = ABOpening(s - 1, bposition, alpha, beta, 1)
            if (input.value < beta):
                beta = input.value
                output.board_state = bposition
            output.count = output.count + input.count
        if(alpha>= beta):
            break
    if (flag == 1):
        output.value = alpha
    else:
        output.value = beta
    return output

board = ReadBoard()
'''
print(board)
board_10 = All_functions.GenerateAdd(board)
board_11 = All_functions.GenerateRemove(board, ['xxxBxWWWWWBBBBxxxx'])
board_12 = All_functions.GenerateHopping(board)
board_13 = All_functions.GenerateMove(board)
board_14 = All_functions.GenerateMovesOpening(board)
board_15 = All_functions.GenerateMovesMidgameEndgame('xxxBxWWWWWBBBBxxxx')
board_16 = GenerateOpeningBlackMoves(board)
board_17 = All_functions.closeMill(2, board)
print("Generate Add:" , board_10)
print("Generate Remove:", board_11)
print( "Generate Hopping",board_12)
print("Generate Move:", board_13)
print("Generate opening:", board_14)
print("Generate MidgameEndgame:", board_15)
print("Generate BlackMoves:", board_16)
print("closeMill", board_17)
'''
output = ABOpening(s,board,minimum, maximum,1)
print("Board Position:", ''.join(output.board_state))
print("Position evaluated by static estimation:",output.count)
print("MINIMAX esitmate:",output.value)
WriteBoard(output.board_state)