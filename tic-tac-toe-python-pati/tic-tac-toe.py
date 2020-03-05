# ---------- Global variables

winner = 0




#------------ How game looks like in code


def tictactoe_game():
    print_board()
    get_move()
    mark()
    has_won()
    is_full()
    winner = 0
    print_result

   
#---------- Functions --------
def init_board():
    board = [[0, 0], [0, 1], [3, 0] ,
             1,0 1, 1,
             0, 0, 0]
    return board


def get_move():
    row =[0,1,2
         ]
    row, col = 0, 0
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


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
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
