"""
Name: Patsy Mejia-Rocha
lab10.py
"""


def build_board():
    game_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return game_list


def display_board(position_list):
    acc = 0
    print('----------')
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print(position_list[acc], end=' | ')
            acc += 1
        print()
    print('----------')


def fill_spot(board, position, marker):
    board[position] = marker


def legal_spot(board, spot):
    if (board[spot] == 'X' or board[spot] == 'O') or (spot < 0 or spot > 9):
        return False
    else:
        return True


def game_won(board):
    winCon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for condition in winCon:
        acc = 0
        for spot in condition:
            if board[spot - 1] == 'X':
                acc += 1
        if acc == 3:
            return 'x_wins'
        acc2 = 0
        for spot in condition:
            if board[spot - 1] == 'O':
                acc2 += 1
        if acc2 == 3:
            return 'o_wins'


def game_over(board, turnCount):
    if (game_won(board) == 'x_wins' or game_won(board) == 'o_wins') or (turnCount > 9):
        return True
    else:
        return False


def play_game():
    position_list = build_board()
    turnCount = 1
    while not game_over(position_list, turnCount):
        display_board(position_list)
        marker = input("X or O? ")
        print("O.K. " + marker + ", ")
        spot = (eval(input("Choose an available position: "))-1)
        if legal_spot(position_list, spot):
            fill_spot(position_list, spot, marker)
            turnCount += 1
        else:
            print("Invalid.")

        if game_won(position_list) == 'o_wins':
            print("O wins!")
        if game_won(position_list) == 'x_wins':
            print("X wins!")



def main():
    play_game()
    pass


main()
