'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    

def square_num(n):
    row = (n - 1) // 3
    column = (n - 1) % 3
    return [row, column]

def put_in_board(board, mark, square_num):
    board[square_num[0]][square_num[1]] = mark

def place_not_valid(place):
    if place > 9 or place < 1:
        return True
    cord = square_num(place)
    return board[cord[0]][cord[1]] != ' '

def get_free_squares(board):
    ret = []
    for row in range(3):
        for column in range(3):
            if(board[row][column] == ' '):
                ret.append([row, column])

    return ret


def make_random_move(board, mark):
    free = get_free_squares(board)
    size = len(free)
    rand = int(size * random.random())
    put_in_board(board, mark, free[rand])

def is_row_all_marks(board, row_i, mark):
    return board[row_i] == [mark] * 3 #make a list of length three with the mark

def is_col_all_marks(board, col_i, mark):
    column = [board[0][col_i], board[1][col_i], board[2][col_i]]
    return column == [mark] * 3

def is_diagnols_all_marks(board, mark):
    return board[0][0] == board[1][1] == board[2][2] == mark or board[0][2] == board[1][1] == board[2][0] == mark

def is_win(board, cord, mark):
    r_win = is_row_all_marks(board, cord[0], mark)
    if r_win:
        return True
    else:
        c_win = is_col_all_marks(board, cord[1], mark)
        if(c_win):
            return True
        else:
            d_win = is_diagnols_all_marks(board, mark)
            return d_win
        

def make_smart_move(board, mark):
    cords = get_free_squares(board)

    for cord in cords:
        #check if place in that cord leads to a win
        put_in_board(board, mark, cord)
        if(is_win(board, cord, mark)):
            return cord
        #undo placement
        put_in_board(board, ' ', cord)

    #if nothing returned yet, put the first coordinate in board
    make_random_move()
    return None

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    moves = 0
    x = True

    # board = [['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    # print(is_row_all_marks(board, 0, 'X'))
    
    while moves < 9:

        mark = 'X' if x else 'O'
        cord = []

        if(x):
            place = int(input("Enter Your Move: "))
            while place_not_valid(place):
                place = int(input("Invalid Move, Enter a New One: "))

            cord = square_num(place)
            put_in_board(board, mark, cord)
        else:
            cord = make_smart_move(board, mark)

        moves += 1
        x = not x

        print_board_and_legend(board)   
        print("\n\n") 

        if(cord != None and is_win(board, cord, mark)):
            print(mark, ' wins!')
            break        
        
