import sys
from typing import final
import All_functions
from copy import deepcopy
maximum = sys.maxsize
minimum = -sys.maxsize
s = int(sys.argv[3])
    
def WriteBoard(out_state):
    board4 = open(sys.argv[2],"w")
    for every in out_state:
        board4.write(every)
    board4.close()

def ReadBoard():
    board3 = open(sys.argv[1],"r")
    board = []
    for long in board3:
        for character in long:
            board.append(character)
    board3.close()
    return board

def StaticEstimationGame(static_board):
    count_of_white = 0
    count_of_black = 0
    static_board = deepcopy(static_board)
    for position in range(0, len(static_board)):
        if(static_board[position]== 'W'):
            count_of_white = count_of_white + 1;   #increementing the count of white
        elif(static_board[position]== 'B'):
            count_of_black = count_of_black + 1;   #increementing the count of black
    p = All_functions.GenerateMovesMidgameEndgameBlack(static_board)
    p_size = len(p)
    if(count_of_black <=2):
        return 10000
    elif(count_of_white<=2):
        return -10000
    else:
        return ((1000)*(count_of_black -  count_of_white)) - p_size
    #static_estimate_opening = count_of_white - count_of_black
    #return static_estimate_opening 

def MiniMaxGameBlack(s, game_board, flag):
    output = All_functions.outputClass()
    input = All_functions.outputClass()
    board_list = []
    if (s == 0):
        final = StaticEstimationGame(game_board)
        output = All_functions.outputClass(final, output.count + 1, game_board)
        return output

    if (flag == 1):
        board_list = All_functions.GenerateMovesMidgameEndgameBlack(game_board)
        output.value = minimum

    else:
        board_list = All_functions.GenerateMovesMidgameEndgame(game_board)
        output.value = maximum

    for bposition in board_list:
        if (flag == 1):
            input = MiniMaxGameBlack(s - 1, bposition, 0)
            if (input.value > output.value):
                output.value = input.value
                output.board_state = bposition
            output.count = output.count + input.count

        else:
            input = MiniMaxGameBlack(s - 1, bposition, 1)
            if (input.value < output.value):
                output.value = input.value
                output.board_state = bposition
            output.count = output.count + input.count

    return output

board = ReadBoard()
output = MiniMaxGameBlack(s,board,1)
print("Board Position:", ''.join(output.board_state))
print("Position evaluated by static estimation:",output.count)
print("MINIMAX esitmate:",output.value)
WriteBoard(output.board_state)