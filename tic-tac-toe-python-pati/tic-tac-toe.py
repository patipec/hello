import sys


# ---------- Global variables

winner = 0
player = 1
board = []

# ------------ How game looks like in code


def tictactoe_game():
    print_board()
    get_move()
    mark()
    has_won()
    is_full()
    winner = 0
    print_result

#  ---------- Functions --------


def init_board():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    return board


def get_move(board, player):
    # give row
    print("Please give row letter: ")
    row_n = input().upper()

    def row_number(row_n):  # convert letter to number
        if row_n == "A":
            row_n = 0
            return(row_n)
        elif row_n == "B":
            row_n = 1
            return(row_n)
        elif row_n == "C":
            row_n = 3
            return(row_n)

    row = row_number(row_n) 
    print("Please give column number: ")  # give col
    col = input()

    def check_if_valid(row, col):
        if row not in (0, 1, 2):
            print("Please give right coordinates, eg. A and 1")
        elif col != "A" or col != "B" or col != "C":
            print("Please give right coordinates, eg. A and 1")

    check_if_valid(row, col)
    col = int(col)
    return(row, col)
    # def if_valid_coords():


# def get_ai_move(board, player):
#     """Returns the coordinates of a valid move for player on board."""
#     row, col = 0, 0
#     return row, col


def mark(board, player, row, col):
    if player == 1:
    


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board():
    print("  1   2   3 ") 
    print("A . | . | . ")
    print("------------")
    print("B . | . | . ")
    print("------------")
    print("C . | . | . ")


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def main_menu():
    tictactoe_game()


if __name__ == '__main__':
    main_menu()
