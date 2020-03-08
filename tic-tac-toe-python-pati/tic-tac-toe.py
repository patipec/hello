import sys
import random

# ---------- Global variables

winner = 0

board = []

# ------------ How game looks like in code


def tictactoe_game(ai):
    player = 1
    board = init_board()
    print_board(board)
    
    while has_won(board, player) is False and is_full(board) is False:
        if player == 1:
            print("X's turn")
        else:
            print("O's turn")
        if ai and player == 2:
            row, col = get_ai_move(board)
        else:
            row, col = get_move(board, player)
        mark(board, player, row, col)
        if has_won(board, player):
            print_result(player)
        elif is_full(board):
            player = 0
            print_result(player)
        if player == 2:
            player = 1
        else:
            player = 2      

#  ---------- Functions --------


def init_board():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    return board


def get_move(board, player):
    row, col = 0, 0
    valid = True
    while valid is True:
        print("Please give row letter or type quit to quit from game: ")
        row_n = input().upper()
        if row_n == "QUIT":
            sys.exit()

        def row_number(row_n):  # convert letter to number
            if row_n == "A":
                row_n = 0
                return(row_n)
            elif row_n == "B":
                row_n = 1
                return(row_n)
            elif row_n == "C":
                row_n = 2
                return(row_n)

        row = row_number(row_n) 
        print("Please give column number: ")  # give col

        try:  # probuje wykonac wprowadzony input i zmienic na int
            col = int(input())-1
        except ValueError:  # podaje jaki blad omijac
            print("Please give right coordinates, eg. A and 1")
            continue  # opusc dalszy kod i wroc do while
        if col not in (0, 1, 2) or row not in (0, 1, 2):
            print("Please give right coordinates, eg. A and 1")
        else:
            valid = False
            if not is_free(board, row, col):
                print("This position is occupated")
                valid = True
    return row, col


def is_free(board, row, col):
    if board[row][col] == 0:
        return True
    else: 
        return False


def get_ai_move(board):
    free = False
    while not free:
        ai_choose_row = random.randint(0, 2)
        ai_choose_col = random.randint(0, 2)
        if is_free(board, ai_choose_row, ai_choose_col):
            row = ai_choose_row
            col = ai_choose_col
            free = True
    return row, col



def mark(board, player, row, col):
    if player == 1:
        board[row][col] = 'X'
        # player = 2
    elif player == 2:
        board[row][col] = 'O'
        # player = 1
    print("After player turn board looks like:  \n")
    print_board(board)


def has_won(board, player):
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") \
            or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") \
            or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"):
        return True
    elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") \
            or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") \
            or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
        return True
    elif (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") \
            or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") \
            or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        return True
    elif (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") \
            or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") \
            or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
        return True
    elif (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") \
            or (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"):
        return True
    elif (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O") \
            or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"):
        return True
    else:
        return False


def is_full(board):
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                return False
    return True



def print_board(board, player=None):
    temp_board = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                temp_board.append('.')
            else:
                temp_board.append(board[i][j])
    print("   1   2   3")
    print("A  {0} | {1} | {2} \n  ---+---+---\n\
B  {3} | {4} | {5} \n  ---+---+---\n\
C  {6} | {7} | {8} \n\
     ".format(temp_board[0], temp_board[1], temp_board[2], temp_board[3], temp_board[4],
          temp_board[5], temp_board[6], temp_board[7], temp_board[8]))
    pass

# funkcja print result ma winnera, który jest tylko na początku określony jako zmienna globalna
# ale funkcja print_result(PLAYER) wprowadza PLAYERA do funkcji print_result(WINNER)
# w ten oto sposób player zamienia sie w winnera


def print_result(winner):
    if winner == 1:
        print("X has won!")
    elif winner == 2:
        print("O has won!")
    else:
        print("It's a draw!")
    pass


def main_menu():
    print("Please choose option:\n")
    print("Choose 1 to start Human - Human game")
    print("Choose 2 to start Human - AI")
    print("To quit write 'quit'")
    choose = input().upper()
    
    if choose == "1":
        tictactoe_game(player=1)
    if choose == "2":
        ai = 2
        tictactoe_game(ai)
        print("To be continued")
    if choose == "QUIT":
        sys.exit()

    


if __name__ == '__main__':
    main_menu()
