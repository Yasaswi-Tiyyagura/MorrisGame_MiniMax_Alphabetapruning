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

def ReadBoard():
    board1 = open(sys.argv[1],"r")
    board = []
    for long in board1:
        for character in long:
            board.append(character)
    board1.close()
    return board

def GenerateOpeningBlackMoves(b):
    tempb = All_functions.SwapBoard(b)
    black_moves_generator = []
    black_moves_generator = All_functions.GenerateAdd(tempb)
    moves_list = []

    for each in range(0, len(black_moves_generator)):
        b = black_moves_generator[each]
        moves_list.insert(each, All_functions.SwapBoard(b))
    return moves_list

def StaticEstimationOpeningBlack(static_board):
    count_of_white = 0
    count_of_black = 0
    static_board = deepcopy(static_board)
    for position in range(0, len(static_board)):
        if(static_board[position]== 'W'):
            count_of_white = count_of_white + 1;   #increementing the count of white
        elif(static_board[position]== 'B'):
            count_of_black = count_of_black + 1;   #increementing the count of black
    static_estimate_opening = count_of_black - count_of_white
    return static_estimate_opening

def MiniMaxOpeningBlack(s, game_board, flag):
    output = All_functions.outputClass()
    input = All_functions.outputClass()
    board_list = []
    if (s == 0):
        final = StaticEstimationOpeningBlack(game_board)
        output = All_functions.outputClass(final, output.count + 1, game_board)
        return output

    if (flag == 1):
        board_list = GenerateOpeningBlackMoves(game_board)
        output.value = minimum

    else:
        board_list = All_functions.GenerateMovesOpening(game_board)
        output.value = maximum

    for bposition in board_list:
        if (flag == 1):
            input = MiniMaxOpeningBlack(s - 1, bposition, 0)
            if (input.value > output.value):
                output.value = input.value
                output.board_state = bposition
            output.count = output.count + input.count

        else:
            input = MiniMaxOpeningBlack(s - 1, bposition, 1)
            if (input.value < output.value):
                output.value = input.value
                output.board_state = bposition
            output.count = output.count + input.count

    return output


      
       

board = ReadBoard()
#print(board)

'''
board_10 = All_functions.GenerateAdd(board)
board_11 = All_functions.GenerateRemove(board, ['xxxBxWWWWWBBBBxxxx'])
board_12 = All_functions.GenerateHopping(board)
board_13 = All_functions.GenerateMove(board)
board_14 = All_functions.GenerateMovesOpening(board)
board_15 = All_functions.GenerateMovesMidgameEndgame('xxxBxWWWWWBBBBxxxx')
board_16 = GenerateOpeningBlackMoves(board)
board_17 = All_functions.closeMill(4, board)
print("Generate Add:" , board_10)
print("Generate Remove:", board_11)
print( "Generate Hopping",board_12)
print("Generate Move:", board_13)
print("Generate opening:", board_14)
print("Generate MidgameEndgame:", board_15)
print("Generate BlackMoves:", board_16)
print("closeMill", board_17)
'''

output = MiniMaxOpeningBlack(s,board,1)
print("Board Position:", ''.join(output.board_state))
print("Position evaluated by static estimation:",output.count)
print("MINIMAX esitmate:",output.value)
WriteBoard(output.board_state)