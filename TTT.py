import random

# Displaying tic tac toe board with indices
def display_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---|---|---')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# Displaying board indices before the game starts
def display_initial_board():
    initial_board = [str(i) for i in range(10)]  # Use string representation of indices
    display_board(initial_board)

# Player chooses marker
def player_input():
    marker = ''

    '''
    OUTPUT =(Player 1 marker, Player 2 marker)
    '''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')  # (player1, player 2)
    else:
        return ('O', 'X')  # (player1, player 2)

# Assigning marker to the index position
def place_marker(board, marker, position):
    board[position] = marker

# To check possibility of mark for win on rows, columns, and diagonals
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

# For randomly choosing player
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Check if space is free available or not
def space_check(board, position):
    return board[position] == ' '

# Checks if board is full or not
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
         position = int(input(f'{turn}, choose your next position: (1-9) '))

    return position

def replay():
    choice = input("Do You Wanna Play Again? [Yes or No] ")
    return choice.lower().startswith('y')

# Running A Game (using while loop)
print('Hey! Welcome to TIC TAC TOE GAME !!!')
display_initial_board()

while True:
    # set up everything (board, who's first, choose markers X, O)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will choose first')

    play_game = input('Are you ready to play [enter yes or no]:')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congrats to Player 1, You won!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Uhhoh....It's a tie!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Congrats to Player 2, You won!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Uhhoh....It's a tie!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
            
          
          
        