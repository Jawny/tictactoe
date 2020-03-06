from random import randrange
from random import choice as rchoice

# game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if you should continue game
continue_game = True

# winner or tie?
winner = None

# Who's turn?
current_player = "X"

# coop = false ai = true
type_of_game = False


# setup two player or AI?
def choice():
    decision = input("Type '1' to play against an AI or '2' for two-player ")
    decision = int(decision)
    if decision == 1:
        start_game_ai()
    elif decision == 2:
        start_game_coop()


# function to display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print('\n')


# start game ai
def start_game_ai():
    # display board
    display_board()
    while continue_game:
        # handle turn for single player
        handle_turn(current_player)
        # check if game is over
        check_if_game_over()
        # flip to ai
        flip_player()
        # handle turn for ai
        handle_turn_ai(current_player)
        # display board
        display_board()
        # check if game is over
        check_if_game_over()
        # flip to player
        flip_player()

    # game is over
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie :(")


def handle_turn_ai(player):
    number_list = list(range(9))
    valid = True
    while valid:
        choice_ai = rchoice(number_list)
        number_list.remove(choice_ai)
        if board[choice_ai] == "-":
            valid = False
    board[choice_ai] = player


# start game coop
def start_game_coop():
    # display board
    display_board()
    while continue_game:
        # handle turn for single player
        handle_turn(current_player)
        # display board
        display_board()
        # check if game is over
        check_if_game_over()
        # flip to other player
        flip_player()

    # game is over
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie :(")


# handle each turn
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1 - 9: ")

    valid = False
    while not valid:
        # TODO replace with regular expressions in the future?
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 - 9: ")
        position = int(position) - 1

        if board[position] != "-":
            print("invalid spot. Try again")
        else:
            valid = True

    board[position] = player


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    # setup global variables
    global winner
    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return


def check_rows():
    global continue_game
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        continue_game = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_columns():
    global continue_game
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        continue_game = False
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return


def check_diagonals():
    global continue_game
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[2] == board[4] == board[6] != "-"

    if dia_1 or dia_2:
        continue_game = False
    if dia_1:
        return board[0]
    if dia_2:
        return board[2]
    return


def check_if_tie():
    global continue_game
    if "-" not in board:
        continue_game = False
    return


def flip_player():
    print('\n')
    global current_player
    # if current player is X change to O
    if current_player == "X":
        current_player = "O"
    # if current player is O change to X
    elif current_player == "O":
        current_player = "X"

    return


# starts game !!
choice()
