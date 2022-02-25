

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
        
    

def fill_board():
    pass

def move():
    pass

def board_completed():
    pass

def win(board):
    if 2048 in board:
        print("CONGRATULATION!! YOU REACHED 2048!!")
        return True
    return False



#TEST GAME
size=4
board= set_board(size)
show_board(board)

test_board= [[0,0,2,2],[0,2,2,2],[0,4,16,0],[4,0,4,0]]

show_board(test_board)

