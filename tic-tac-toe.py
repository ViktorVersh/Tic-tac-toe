"""
Игра крестики нолики
"""
# ----------------- Игровое поле ------------------
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_state(state):
    """
    Функция отрисовки игрового поля
    :param state:
    :return:
    """
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')


# ---------------- выигрышные комбинации ----------------------------------
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def get_winner(state, combinations):
    """
    Функция проверки выигрыша
    :param state:
    :param combinations:
    :return:
    """
    for (x, y, z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
    return ''


def is_draw(state):
    """
    Функция проверки на ничью
    :param state:
    :return:
    """
    return ' ' not in state


def play_game(board_):
    """
    Функция запуска игры
    :param board_:
    :return:
    """
    current_sign = 'X'
    while get_winner(board_, winning_combinations) == '':
        index = int(input(f'Введите индекс клетки (от ноля до девяти), куда хотите сделать ход: {current_sign}?'))
        if index < 0 or index > 8:
            print(f'Вы ввели неверный индекс {index}. Введите от 0 до 9')
            continue
        board_[index] = current_sign

        print_state(board_)
        print()
        # Проверка выигрыша
        winner_sign = get_winner(board_, winning_combinations)
        if winner_sign != '':
            print_state(board_)
            print(f'Победили в игре: {winner_sign}!')
            break
        # Проверки ничьей
        if is_draw(board_):
            print_state(board_)
            print('Ничья!')
            break

        current_sign = 'X' if current_sign == 'O' else 'O'


play_game(board)
