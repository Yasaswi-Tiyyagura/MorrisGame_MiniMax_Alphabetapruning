from copy import deepcopy

class outputClass(object):
    count = 0
    value = 0
    board_state = list()
    
    def __init__(self,value=0,count=0,board_state=list()):
        self.count = count
        self.value = value
        self.board_state = board_state

def neighbors_list(j):  #brute force method
    switch_case = {
      0: [1,2,15],
      1: [3,8,0],
      2: [0,4,3,12],
      3: [1,2,5,7],
      4: [2,5,9],
      5: [4,6,3],
      6: [5,7,11],
      7: [6,8,3,14],
      8: [1,17,7],
      9: [4,10,12],
      10: [9,11,13],
      11: [6,10,14],
      12: [9,15,13,2],
      13: [10,12,14,16],
      14: [7,11,13,17],
      15: [0,16,12],
      16: [13,15,17],
      17: [14,16,8]  }
    
    return switch_case.get(j,"not valid case")  #returns list of locations corresponding to j's neighbors

'''

def neighbours(int i):
switch (i) {
 case 0:
  return { 1,2,15 };
 case 1:
  return { 3,8,0 };
 case 2:
  return { 0,4,3,12 };
 case 3:
  return { 1,2,5,7 };
 case 4:
  return { 2,5,9 };
 case 5:
  return { 4,6,3 };
 case 6:
  return { 5,7,11 };
 case 7:
  return { 6,8,3,14 };
 case 8:
  return { 1,17,7 };
 case 9:
  return { 4,10,12 };
 case 10:
  return { 9,11,13 };
 case 11:
  return { 6,10,14 };
 case 12:
  return { 9,15,13,2 };
 case 13:
  return { 10,12,14,16 };
 case 14:
  return { 7,11,13,17 };
 case 15:
  return { 0,16,12 };
 case 16:
  return { 13,15,17 };
 case 17:
  return { 14,16,8 };
 default:
  return {};}
'''

def closeMill(j_location,b):

    C = b[j_location]

    if(C == 'W' or C == 'B'):
        if(j_location==0):
            if((b[2]==C and b[4]==C)):
                return True
    
        elif(j_location==1):
            if((b[8]==C and b[17]==C) or (b[3]==C and b[5]==C)):
                return True
        
        elif(j_location==2):
            if((b[0]==C and b[4]==C)):
                return True
        
        elif(j_location==3):
            if((b[7]==C and b[14]==C) or (b[1]==C and b[5]==C)):
                return True
        
        elif(j_location==4):
            if((b[0]==C and b[2]==C)):
                return True

        elif(j_location==5):
            if((b[6]==C and b[11]==C) or (b[1]==C and b[3]==C)):
                return True   
        
        elif(j_location==6):
            if((b[5]==C and b[11]==C) or (b[7]==C and b[8]==C)):
                return True
        
        elif(j_location==7):
            if((b[6]==C and b[8]==C) or (b[3]==C and b[14]==C)):
                return True
        
        elif(j_location==8):
            if((b[6]==C and b[7]==C) or (b[1]==C and b[17]==C)):
                return True
        
        elif(j_location==9):
            if((b[12]==C and b[15]==C) or (b[10]==C and b[11]==C)):
                return True

        elif(j_location==10):
            if((b[9]==C and b[11]==C) or (b[13]==C and b[16]==C)):
                return True
        
        elif(j_location==11):
            if((b[9]==C and b[10]==C) or (b[5]==C and b[6]==C) or (b[14]==C and b[17]==C)):
                return True
        
        elif(j_location==12):
            if((b[9]==C and b[15]==C) or (b[13]==C and b[14]==C) ):
                return True
        
        elif(j_location==13):
            if((b[12]==C and b[14]==C) or (b[16]==C and b[10]==C)):
                return True    
        
        elif(j_location==14):
            if((b[12]==C and b[13]==C) or (b[3]==C and b[7]==C) or (b[17]==C and b[11]==C)):
                return True
        
        elif(j_location==15):
            if((b[16]==C and b[17]==C) or (b[12]==C and b[9]==C)):
                return True
        
        elif(j_location==16):
            if((b[15]==C and b[17]==C) or (b[13]==C and b[10]==C)):
                return True

        elif(j_location==17):
            if((b[15]==C and b[16]==C) or (b[8]==C and b[1]==C) or (b[14]==C and b[11]==C)):
                return True
    else:
          return False

    return False


def GenerateRemove(board_position, L):
    for location in range(0, len(board_position)):  # for each location in the board
        if(board_position[location] == 'B'):  # if board location is black
            if(closeMill(location, board_position) == False):
                b = deepcopy(board_position)
                b[location] = 'x'
                L.append(b)
            else:
                b = deepcopy(board_position)
                L.append(b)
    return L

def GenerateHopping(board_position):
    board_positions_list = list()
    for location_alpha in range(0, len(board_position)):  # for each location in the board
        if(board_position[location_alpha] == 'W'):  # if board location of alpha is W
            for location_beta in range(0, len(board_position)):
                if(board_position[location_beta] == 'x'):  # if board location of beta is empty
                    b = deepcopy(board_position)
                    b[location_alpha] = 'x'
                    b[location_beta] = 'W'
                    if closeMill(location_beta, b):
                        GenerateRemove(b, board_positions_list)
                    else:
                        board_positions_list.append(b)


def GenerateAdd(board_position):

    board_positions_list = list()
    for location in range(0, len(board_position)):  # for each location in the board
        
        if(board_position[location] == 'x'):  # if board location is empty

            b = deepcopy(board_position)

            b[location] = 'W'
            
            if closeMill(location, b):
                board_positions_list = GenerateRemove(b, board_positions_list)
            else:
                board_positions_list.append(b)
                
    return board_positions_list

def GenerateMove(board_position):
    board_positions_list = list()
    for location in range(0, len(board_position)):  # for each location in the board
        if(board_position[location] == 'W'):  # if board location is white
            n = neighbors_list(location)
            for j in n:
                if(board_position[j] == 'x'):  # if board location is empty
                    b = deepcopy(board_position)
                    b[location] = 'x'
                    b[j] = 'W'
                    if closeMill(j, b):
                        GenerateRemove(b, board_positions_list)
                    else:
                         board_positions_list.append(b)
                         
    return board_positions_list


def GenerateMovesOpening(board_position):
    board_positions_list = list()
    board_positions_list = GenerateAdd(board_position)
    return board_positions_list #returns the list of board positions
    
def GenerateMovesMidgameEndgame(board_position):
    board_positions_list = list()  # creating a list
    count_of_white = 0     #assigning the white count to 0
    for board_place in range(0, len(board_position)):   
        if(board_position[board_place]== 'W'):
            count_of_white = count_of_white + 1;   #increementing the count of white 
    if(count_of_white <= 3): 
        board_positions_list = GenerateHopping(board_positions_list) # return the list resulted by GenerateHopping
        return board_positions_list
    else:
        board_positions_list = GenerateMove(board_positions_list) # return the list resulted by GenerateMove
        return board_positions_list 


def SwapBoard(flip_board):
    b = list(range(0,18))
    flip_board = deepcopy(flip_board)
    for pos in range(0,len(flip_board)):
        if(flip_board[pos]=='W'):
            b[pos]='B'
        elif(flip_board[pos]=='B'):
            b[pos]='W'
        else:
            b[pos]='x'
    return b

def GenerateMovesMidgameEndgameBlack(board_position):
    temp = SwapBoard(board_position)
    L = list()
    listofPositions = GenerateMovesMidgameEndgame(temp)
    for positions in range(0,len(listofPositions)):
        b = listofPositions[positions]
        L.insert(positions, SwapBoard(b))
    return L

#GenerateMovesOpeningBlack
def generateMoveOpeningBlack(b):
    tempb = SwapBoard(b)
    black_moves = list()
    black_moves = GenerateAdd(tempb)
    moves = list()
    
    for each in range(0,len(black_moves)):
        b = black_moves[each]
        moves.insert(each,SwapBoard(b))
    return moves 








    
