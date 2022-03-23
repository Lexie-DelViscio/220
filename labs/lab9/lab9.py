"""
Name: Lexie DelViscio
File Name: lab9.py
Problem Description: This program creates a function using multiple smaller defined functions so in order to create
the game tictactoe.
Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""


def build_board():
    board = []
    for i in range(1, 10):
        board += [i]
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    position_index = position - 1
    return str(board[position_index]).isnumeric()


def fill_spot(board, position, character):
    position_index = position - 1
    character = character.strip().lower()
    board[position_index] = character


def winning_game(board):
    for i in range(0, len(board), 3):
        if board[i] == board[i + 1] == board[i + 2]:
            return True
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6]:
            return True
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True
    else:
        return False


def game_over(board):
    if winning_game(board):
        return True
    for i in range(len(board)):
        if is_legal(board, i + 1):
            return False
    return True


def get_winner(board):
    x = 0
    o = 0
    for i in range(len(board)):
        if board[i] == 'x':
            x += 1
        elif board[i] == 'o':
            o += 1
    if not game_over(board):
        return None
    elif x > o:
        return 'x'
    elif x == o:
        return 'o'


def play(board):
    print("Welcome to Tic Tac Toe!\n Enter a position to place your shape there on the board.\n "
          "you win when you get three in a row!\nx's always go first!.")
    playing_variable = "y"
    character_string = 'xo'
    character_index = 0
    while playing_variable[0] == 'y' or playing_variable[0] == 'Y':
    # hey! you checked my work in lab and couldnt figure out why it was still repeating after no was entered
        while not game_over(board):
            print_board(board)
            position = eval(input("{}'s, choose a position: ".format(character_string[character_index])))
            while not is_legal(board, position):
                print('that position is not available choose a new position')
                position = eval(input("{}'s, choose a position: ".format(character_string[character_index])))
            else:
                character = character_string[character_index]
                fill_spot(board, position, character)
            if winning_game(board):
                print_board(board)
                print(get_winner(board), "'s win!")
                playing_variable = input("play again: ")
                board = build_board()
                character_index = 1
            if game_over(board) and not winning_game(board):
                print('Tie')
                playing_variable = input("play again: ")
                board = build_board()
                character_index = 1
            character_index = character_index + 1
            character_index = character_index % 2


def main():
    board = build_board()
    play(board)


if __name__ == '__main__':
    main()
