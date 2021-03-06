#Working Properly
import ai
from os import system


possible_move = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
list_of_done_move=[]

#Help

def help():
    c = 1
    board=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(ai.DIMENSION):
        for j in range(ai.DIMENSION):
            board[i][j]=c
            c+=1
    return board

def print_help(board):
    wall = "*-----**-----**-----*"
    
    for i in range(ai.DIMENSION):
        print(wall)
        print("|  "+str(board[i][0])+'  '+'||  '+str(board[i][1])+'  ||  '+str(board[i][2])+'  |')
    print(wall)

def clear():
    system("clear")

#Input Related Method
def IsValidChoice(num):
    if(num>0 and num<=9):
        return True
    return False
def mapInt2Pos(num):
    x,y = possible_move[num-1]
    return x,y

def moveToInt(x,y):
    if x==0:
        if y == 0:
            return 1
        if y == 1:
            return 2
        if y == 2:
            return 3
    if x==1:
        if y == 0:
            return 4
        if y == 1:
            return 5
        if y == 2:
            return 6
    if x==2:
        if y == 0:
            return 7
        if y == 1:
            return 8
        if y == 2:
            return 9
    
#Game
def keepTrack_TakenMove(list_of_done_move,move):
    if ((list_of_done_move)==[]):
        return False
    else:
        for i in list_of_done_move:
            if move==i:
                return True
    
    return False
    
def take_player_move(list_of_done_move):     
    num = int(input("Enter Your Move"))
    ans = IsValidChoice(num)
    check = keepTrack_TakenMove(list_of_done_move,num)
    if(ans==True and check==False):
        list_of_done_move.append(num)
        x,y =mapInt2Pos(num)
        return x,y
    while(ans!=True or  check==True):
        print("Enter valid Movement")
        num = int(input("Enter Your Move"))
        ans = IsValidChoice(num)
        check = keepTrack_TakenMove(list_of_done_move,num)
        list_of_done_move.append(num)
    x,y =mapInt2Pos(num)
    return x,y

def computer_move(board):
    x,y = ai.find_Move(board)
    return x,y

def put_move(board,x_coord,y_coord,choice):
    if(choice==ai.HUMAN):
        board[x_coord][y_coord]=ai.HUMAN
    else:
        board[x_coord][y_coord]=ai.COMPUTER 

def start_game(board,h_board,list_of_done_move):
    score = ai.check_board(board)
    if(score == 1):
        print("Computer Has Won The match")
        return 1
    elif score == -1:
        print("Human has won the match")
        return -1
    else:
        while(score!=-1 or score!=1):
            
            x,y = take_player_move(list_of_done_move)
            put_move(board,x,y,ai.HUMAN)
            clear()
            print_help(h_board)
            ai.print_board(board)
            x,y = computer_move(board)
            
            if(x!=-1 and y!=-1):
                num = moveToInt(x,y)
                list_of_done_move.append(num)
                put_move(board,x,y,ai.COMPUTER)
            clear()
            print_help(h_board)
            ai.print_board(board)
            score = ai.check_board(board)
            if(score==-1):
                print("Human won the match")
                ai.print_board(board)
                return -1
            if(ai.Is_board_Empty(board)==False and score == 0):
                print("Game is tie!!")
                ai.print_board(board)
                return 0
            if(score==1):
                print("Computer won the match")
                return 1
            
            
            
if __name__=='__main__':
    board = ai.init_board()
    h_board = help()
    print_help(h_board)
    ai.print_board(board)
    
    start_game(board,h_board,list_of_done_move)
