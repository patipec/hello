import re, sys, random, time


def init_board(): # DONE!
    """Returns an empty 3-by-3 board (with zeros)."""
    # board = [[0]*3]*3
    # board = [['.','.','.'],['.','.','.'],['.','.','.']]
    board = [[0,0,0],[0,0,0],[0,0,0]]
    # board = [[0,'X','O'],[0,'X',0],[0,'O',0]]

    # print('new board: ', board)
    # board = [[0,1,2],[3,4,5],[6,7,0]]
    return board

def get_move(board, player):  # DONE!
   
    def convert_row_to_number(row_argument):# DONE!
        if row_argument == 'A':
            row_argument = 0
            return row_argument
        if row_argument == 'B':
            row_argument = 1
            return row_argument
        if row_argument == 'C':
            row_argument = 2
            return row_argument
    
    def all_possible_fields():  # Prints all possible fields to make a move
        print('Please select one of the free positions: ')
        temp_list = []
        temp_board = [item for elem in board for item in elem]
        for i in range(9):
            if i//3 == 0 and temp_board[i] == 0:
                temp_list.append('A'+str((i%3)+1))
            elif i//3 == 1 and temp_board[i] == 0:
                temp_list.append('B'+str((i%3)+1))
            elif i//3 == 2 and temp_board[i] == 0:
                temp_list.append('C'+str((i%3)+1))
        
        return temp_list

    def check_out_of_range():  # Check if user didn't input something wierd   1 lvl check
        row = input('\nWhat is row you want to put your move (A-B-C):  ')
        col = input('\nWhat is column you want to put your move (1-2-3):  ')
        while ((row == 'A' or row == 'B' or row == 'C') and (col == '1' or col == '2' or col == '3')) == False:
            print('PLEASE PUT PROPER VALUES!')
            print(all_possible_fields())
            row = input('\nWhat is row you want to put your move (A-B-C):  ')
            col = input('\nWhat is column you want to put your move (1-2-3):  ')
        return row, col


    
    def check_if_field_is_free(board, row, col): # Check if user didn't choose occiupied fields -- 2 lvl check
        row_int = convert_row_to_number(row)
        return board[row_int][int(col)-1] == 'X' or board[row_int][int(col)-1] =='O'

    def validate(board):# DONE!
        row, col = check_out_of_range()
        secondLvl = check_if_field_is_free(board, row, col)
        if secondLvl == True:
            print('PLEASE CHOOSE ONE OF FREE FIELDS ON THE BOARD!!!!')
            print(all_possible_fields())
        while secondLvl == True:
            row, col = check_out_of_range()
            secondLvl = check_if_field_is_free(board, row, col)
            if secondLvl == True:
                print('PLEASE CHOOSE ONE OF FREE FIELDS ON THE BOARD!!!!')
                print(all_possible_fields())
        return row, col

    row, col = validate(board)
    return convert_row_to_number(row), int(col)-1
   

def get_ai_move(board, player):
    boardX = random.randint(0,2)
    boardY = random.randint(0,2)
    time.sleep(1)
    while board[boardX][boardY] != 0:
        boardX = random.randint(0,2)
        boardY = random.randint(0,2)
    
    if player == 1:
        board[boardX][boardY] = 'X'
    else:
        board[boardX][boardY] = 'O'
    pass


def mark(board, player, row, col): # Done

    print('first board: ', board)
    if player == 1:
        board[row][col] = 'X'
        # player = 2
    elif player == 2:
        board[row][col] = 'O'
        # player = 1
    # print(board)
    print('gracz', player)
    return board, player


def has_won(board, player):  # DONE

    if player == 1:
        mark = 'X'
    elif player == 2:
        mark = 'O'
    # checking horizontal
    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return player, False
    if board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return player, False
    if board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return player, False
    
    # checking vertical
    if board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return player, False
    if board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return player, False
    if board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return player, False

    # cross checking
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return player, False
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return player, False
    
    return player, True
    

def switch_player(player): # Done
    #switching player if none of condition were complited
    if player == 1:
        return 2
    else:
        return 1



def is_full(board): # DONE
    temp_board = [item for elem in board for item in elem]
    checkLength = len(list(filter(lambda x: (x == 'O' or x == 'X'),temp_board)))
    return checkLength == 9


def print_board(board): # DONE
    """Prints a 3-by-3 board on the screen with borders."""
    print('   1   2   3')
    for i in range(len(board)):
        if i<=len(board)-2:
            var = str(chr(65+i) + '  ' + ' | '.join(map(str, board[i])) + '\n  ---+---+---')
            print(re.sub(r"0", ".", var))
        elif i==len(board)-1:
            var = str(chr(65+i) +'  '+ ' | '.join(map(str, board[i]))+'\n')
            print(re.sub(r"0", ".", var))

    pass


def print_result(winner, who_plays=None): #Done
    if winner == 0:
        return 'No one has won this game DRAW!'
    elif winner == 1:
        return "Congratulates the winner is {} !!!!".format(who_plays[0])
    elif winner == 2:
        return "Congratulates the winner is {} !!!!".format(who_plays[1])


def tictactoe_game(mode='HUMAN-HUMAN'):#DONE
    board = init_board()
    play = 1

    if mode == 'HUMAN-HUMAN':
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
        while is_full(board) != True:
            row, col = get_move(board, 1)
            board, play =  mark(board, play, row, col)
            print_board(board)
            play, flaga = has_won(board, play)
            if flaga == False:
                print(print_result(play,['Player1', 'Player2']))
                break
            if is_full(board) == True:
                print(print_result(0,['Player1', 'Player2']))
                break
            play = switch_player(play)

    elif mode == 'HUMAN-AI': #DONE
        #Human is X 
        #Computer is O
        play = 1
        while is_full(board) != True:
            if play == 1:
                row, col = get_move(board, 1)
                board, play =  mark(board, 1, row, col)
                play, flaga = has_won(board, play)
            elif play == 2:
                get_ai_move(board, 2)

            print_board(board)
            play, flaga = has_won(board, play)
            if flaga == False:
                print(print_result(play,['Player', 'Computer']))
                break
            if is_full(board) == True:
                print(print_result(0,['Player', 'Computer']))
                break
            play = switch_player(play)
        
    elif mode == 'AI-HUMAN':    #DONE
        #Human is O
        #Computer is X
        play = 1
        while is_full(board) != True:
            if play == 2:
                row, col = get_move(board, 2)
                board, play =  mark(board, 2, row, col)
                play, flaga = has_won(board, play)
            elif play == 1:
                get_ai_move(board, 1)
                
            print_board(board)
            play, flaga = has_won(board, play)
            if flaga == False:
                print(print_result(play, ['Computer','Player']))
                break
            if is_full(board) == True:
                print(print_result(0))
                break
            play = switch_player(play)

        
    elif mode == 'AI-AI': #DONE

        play = 1
        while is_full(board) != True:
            get_ai_move(board, play)
            print_board(board)
            play, flaga = has_won(board, play)
            if flaga == False:
                print(print_result(play,['Computer 1','Computer 2']))
                break
            if is_full(board) == True:
                print(print_result(0))
                break
            play = switch_player(play)

def main_menu():
    # tictactoe_game('HUMAN-HUMAN')

    print('1. Human vs Human')
    print('2. Human vs AI')
    print('3. AI vs Human')
    print('4. AI vs AI')
    print('5. Quit game')

    select = input('Select mode: ')

    if select == str(1):
        tictactoe_game('HUMAN-HUMAN')
    elif select == str(2):
        tictactoe_game('HUMAN-AI')
    elif select == str(3):
        tictactoe_game('AI-HUMAN')
    elif select == str(4):
        tictactoe_game('AI-AI')
    elif select == str(5):
        quit()

        

if __name__ == '__main__':
    while True:
        main_menu()

