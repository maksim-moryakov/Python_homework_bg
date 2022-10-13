# Создайте программу для игры в ""Крестики-нолики""

board = list(range(1, 10))

# функция рисует игровое поле
def draw_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|',
              board[2 + i * 3], '|')
        print('-------------')


draw_board(board)


# функция принимает ввод пользователя

def take_input(player):
    valid = False
    while not valid:
        player_answer = input('Куда поставит ' + player +'?')
        try:
            player_answer = input(player_answer)
        except:
            print('Введено не число.')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in 'XO'):
                board[player_answer-1] = player
                valid = True
            else:
                print('Это место занято.')
        else:
            print('Неверное число, нужно ввести число от 1 до 9')


# функция проверки игрового поля

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1] == board[2]]:
            return board[each[0]]
    return False


#  основная функция игры

def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        count += 1
        if count > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, 'Win!')
                win = True
                break
        if count == 9:
            print('Draw!')
            break
    draw_board(board)
main(board)


input('Press Enter to exit!')

exit()
X = "X"
O = "O"
EMPTY = ' '
TIE = "Ничья"
NUM_SQUARES = 9


def display_instruct():
    '''Выводит на экран иснтрукцию для игрока'''
    print(
        """
Добро пожаловать в игру Крестики-нолики!
Это игра с компьютером.
Чтобы сделать свой ход, введите от число от 0 до 8.
Числа соответсвуют полям доски:
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
"""
    )


def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    go_first = ask_yes_no("Хочешь сделать первый ход?(y/n): ")
    if go_first == "y":
        print("\n Ходи, ты играешь крестиками")
        human = X
        computer = O
    else:
        print("\n Спасибо, что предоставил право хода компьютеру")
        computer = X
        human = O
    return computer, human


def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t",  "---------")
    print("\n\t", board[3], "|", board[4],  "|", board[5])
    print("\t",  "---------")
    print("\n\t", board[6], "|", board[7],  "|",  board[8], "\n")


def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number(
            "Твой ход. Выбери одно из полей (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\n Будь внимательней, это поле уже занято. Выбери другое.\n")
    print("Хорошо.....")
    return move


def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    print("Я выберу номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Победил компьютер!")
    elif the_winner == human:
        print("Поздравляю,Вы победили компьютер!")
    elif the_winner == TIE:
        print("Ничья!")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()
input("\n\nНажмите Enter, чтобы выйти.")
