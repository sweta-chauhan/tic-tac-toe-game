DIMENSION = 3
HUMAN = 'X'
COMPUTER = 'O'

def Is_board_Empty(board):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if(board[i][j]=='_'):
                return True
    return False
def check_board(board):
    for row in range(DIMENSION):
        if(board[row][0]==board[row][1] and board[row][1]==board[row][2]):
            if(board[row][0]==COMPUTER):
                
                return 1
            if(board[row][0]==HUMAN):
                return -1
    for col in range(DIMENSION):
       if(board[0][col]==board[1][col] and board[1][col]==board[2][col]):
           if(board[0][col]==COMPUTER):
               
               return 1
           if(board[0][col]==HUMAN):
               return -1
    if(board[0][0]==board[1][1] and board[1][1] == board[2][2]):
        if(board[0][0]==COMPUTER):
            return 1
        if(board[0][0]==HUMAN):
            return -1
    if(board[0][2]==board[1][1] and board[1][1] == board[2][0]):
        if(board[0][2]==COMPUTER):
            return 1
        if(board[0][2]==HUMAN):
            return -1
    return 0

def minmax(board,turn,depth):
    score = check_board(board)
    if(score ==1):
        return 10
    if(score == -1):
        return -10
    if(Is_board_Empty(board)==True ):
        if(turn== True):
            bestVal = -100
            for i in range(DIMENSION):
                for j in range(DIMENSION):
                    if(board[i][j]=='_' and depth<9):
                        
                        board[i][j]=COMPUTER
                        val=minmax(board,not(turn),depth+1)
                        if(val!=None):
                            bestVal = max(bestVal,val)
                        board[i][j]='_'
            return bestVal
        else:
            bestVal = 100
            for i in range(DIMENSION):
                for j in range(DIMENSION):
                    if(board[i][j]=='_' and depth<9):
                        board[i][j]=HUMAN
                        val=minmax(board,not(turn),depth+1)
                        
                        if(val!=None):
                            bestVal = min(bestVal,val)
                        board[i][j]='_'
            return bestVal
        return 0

def find_Move(board):
    x,y=-1,-1
    bestVal = -100
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if(board[i][j]=='_'):
                board[i][j]='O'
                val = minmax(board,False,0)
                board[i][j]='_'
                if(val > bestVal):
                    x,y=i,j
                    bestVal = val
                        
    return x,y
                        

def print_board(board):
    wall = "*-----**-----**-----*"
    
    for i in range(DIMENSION):
        print(wall)
        print("|  "+board[i][0]+'  '+'||  '+board[i][1]+'  ||  '+board[i][2]+'  |')
    print(wall)

def init_board():
    board=[]
    elem=[]
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            elem.append('_')
        board.append(elem)
        elem=[]
    return board
