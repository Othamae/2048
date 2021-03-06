import random
import copy

#2048

# ___________________________
#|      |      |      |      |
#| 2048 | 2048 | 2048 | 2048 |
#|______|______|______|______|
#|      |      |      |      |
#| 2048 | 2048 | 2048 | 2048 |
#|______|______|______|______|
#|      |      |      |      |
#| 2048 | 2048 | 2048 | 2048 |
#|______|______|______|______|
#|      |      |      |      |
#| 2048 | 2048 | 2048 | 2048 |
#|______|______|______|______|




def set_board(size):

    board=[]
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(0) 
    fill_board(board)
    return board

  
def show_board(board):   
    largest = board[0][0]
    for row in board:
        for elem in row:
            if elem>largest:
                largest=elem
    spaces= len(str(largest))
    print(" "+("_"*len(board))*(spaces+2)+ ("_"*4)) 
    for row in board:
        print(("|"+" "*(spaces+2))*4+ "|")
        curr="|"
        for elem in row:
            if elem==0:
                curr+= " "*(spaces+1) + " |"
            else:
                curr+= " "*(spaces+1-len(str(elem)))+str(elem) + " |"                 
        print(curr)
        print(("|"+"_"*(spaces+2))*4+"|") 
      

def fill_board(board):  
    counter=0    
    while counter<2:
        if board_completed(board) and not any_move(board):
            break
        else:
            y= random.randint(0, len(board[0])-1)
            x= random.randint(0, len(board[0])-1)
            if board_completed(board):
                    break 
            if board[y][x]==0:
                board[y][x]=pick_number()
                counter+=1 
                  

def pick_number():
    if random.randint(1,8)==1:
        return 4
    else:
        return 2

def turn(board,move):
    board_copy = copy.deepcopy(board)
    if move == "w":
        board= move_up(board)
    elif move == "s":
        board= move_down(board)
    elif move == "a":
        board= move_left(board)
    elif move == "d":
        board= move_right(board)
    else:
        input("You enter a wrong value, please enter w/a/s/d: ")
    
    if board == board_copy:
        print("Try a different direction!")

    return show_board(board)

def move_up(board):
    added=[]
    mov=False
    for row in range(len(board)):
        for j in range(len(board)):
            for i in range(1,len(board[j])):
                if board[i][j]!=0:
                    if board[i-1][j]==0:
                        board[i-1][j]=board[i][j]
                        board[i][j]=0
                        mov = True
                    elif board[i-1][j]==board[i][j] and (i-1, j) not in added and (i, j) not in added:
                        board[i-1][j]*=2
                        board[i][j]=0
                        mov= True
                        added.append((i-1, j))
    if mov:
        fill_board(board)
    return board      
    

def move_down(board):
    added=[]
    mov=False
    for row in range(len(board)):
        for j in range(len(board)):
            for i in range(len(board[j])-2, -1, -1):
                if board[i][j]!=0:
                    if board[i+1][j]==0:
                        board[i+1][j]=board[i][j]
                        board[i][j]=0
                        mov = True
                    elif board[i+1][j]==board[i][j] and (i+1, j) not in added and (i, j) not in added:
                        board[i+1][j]*=2
                        board[i][j]=0
                        mov= True
                        added.append((i+1, j))
    if mov:
        fill_board(board)
    return board

def move_left(board):
    added=[]
    mov=False
    for row in range(len(board)):
        for i in range(len(board)):
            for j in range(1,len(board[i])):
                if board[i][j]!=0:
                    if board[i][j-1]==0:
                        board[i][j-1]=board[i][j]
                        board[i][j]=0
                        mov = True
                    elif board[i][j-1]==board[i][j] and (i, j-1) not in added and (i, j) not in added:
                        board[i][j-1]*=2
                        board[i][j]=0
                        mov= True
                        added.append((i, j-1))
    if mov:
        fill_board(board)
    return board

def move_right(board):
    added=[]
    mov=False
    for row in range(len(board)):
        for i in range(len(board)):
            for j in range(len(board[i])-2, -1, -1):
                if board[i][j]!=0:
                    if board[i][j+1]==0:
                        board[i][j+1]=board[i][j]
                        board[i][j]=0
                        mov = True
                    elif board[i][j+1]==board[i][j] and (i, j+1) not in added and (i, j) not in added:
                        board[i][j+1]*=2
                        board[i][j]=0
                        mov= True
                        added.append((i, j+1))
    if mov:
        fill_board(board)
    return board

def board_completed(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                return False                
    return True

def any_move(board):
    res= False
    for i in range(len(board)):
        for j in range(len(board)-1):
            if board[i][j]==board[i][j+1]:
                res= True
    
    for i in range(len(board)-1):
        for j in range(len(board)):
            if board[i][j]==board[i+1][j]:
                res= True
    return res

def win(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==2048:
                print("CONGRATULATION!! YOU REACHED 2048!!")
                return True
    return False



# #GAME
size = 4
board = set_board(size)
show_board(board) 
movements = True
winner = False
while movements:      
    move= input("w/a/s/d: ")
    turn(board,move)   
    if win(board) and not winner:
        winner = True 
        continue_playing= input("Do you want to continue? (y): ")
        if continue_playing!= "y":
            break

    if board_completed(board) and not any_move(board):
        print("GAME OVER!!")
        break



# #TEST GAME
# size=4
# board= set_board(size)
# show_board(board)

# test_board= [[2,2048,3,5],[5,4,7,2],[2,3,4,5],[9,2,7,9]]

# show_board(test_board)
# print("Win? ", win(test_board))
# print("Completed? ", board_completed(test_board))
# print("Any move? ", any_move(test_board))
# if board_completed(test_board) and not any_move(test_board):
#     print("GAME OVER")
# test_board= move_up(test_board)
# show_board(test_board)
# fill_board(test_board)
# show_board(test_board)


