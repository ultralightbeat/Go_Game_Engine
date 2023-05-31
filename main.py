
def eprint(*args, **kwargs): print(*args, file=sys.stderr, **kwargs)


import sys
import random

VERSION = '1.0'
# 0000 => 0 пустая ячейка
# 0001 => 1 черный камень
# 0010 => 2 белый камень
# 0100 => 4 каменный маркер
# 0111 => 7 ячейка за досткой
# 1000 => 8 маркер свобод

# 9x9 доска Го
board_9x9 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 1, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 2, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 2, 1, 2, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 9x9 координаты
coords_9x9 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
]

# 13x13 доска Го
board_13x13 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 13x13 координаты
coords_13x13 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A13', 'B13', 'C13', 'D13', 'E13', 'F13', 'G13', 'H13', 'J13', 'K13', 'L13', 'M13', 'N13', 'XX',
    'XX', 'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12', 'J12', 'K12', 'L12', 'M12', 'N12', 'XX',
    'XX', 'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11', 'J11', 'K11', 'L11', 'M11', 'N11', 'XX',
    'XX', 'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 'J10', 'K10', 'L10', 'M10', 'N10', 'XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'K9', 'L9', 'M9', 'N9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'K8', 'L8', 'M8', 'N8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'K7', 'L7', 'M7', 'N7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'K6', 'L6', 'M6', 'N6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'K5', 'L5', 'M5', 'N5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'K4', 'L4', 'M4', 'N4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'K3', 'L3', 'M3', 'N3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'K2', 'L2', 'M2', 'N2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'K1', 'L1', 'M1', 'N1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
]

# 19x19 доска Го
board_19x19 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 19x19 координаты
coords_19x19 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'XX',
    'XX', 'A19', 'B19', 'C19', 'D19', 'E19', 'F19', 'G19', 'H19', 'J19', 'K19', 'L19', 'M19', 'N19', 'O19', 'P19',
    'Q19', 'R19', 'S19', 'T19', 'XX',
    'XX', 'A18', 'B18', 'C18', 'D18', 'E18', 'F18', 'G18', 'H18', 'J18', 'K18', 'L18', 'M18', 'N18', 'O18', 'P18',
    'Q18', 'R18', 'S18', 'T18', 'XX',
    'XX', 'A17', 'B17', 'C17', 'D17', 'E17', 'F17', 'G17', 'H17', 'J17', 'K17', 'L17', 'M17', 'N17', 'O17', 'P17',
    'Q17', 'R17', 'S17', 'T17', 'XX',
    'XX', 'A16', 'B16', 'C16', 'D16', 'E16', 'F16', 'G16', 'H16', 'J16', 'K16', 'L16', 'M16', 'N16', 'O16', 'P16',
    'Q16', 'R16', 'S16', 'T16', 'XX',
    'XX', 'A15', 'B15', 'C15', 'D15', 'E15', 'F15', 'G15', 'H15', 'J15', 'K15', 'L15', 'M15', 'N15', 'O15', 'P15',
    'Q15', 'R15', 'S15', 'T15', 'XX',
    'XX', 'A14', 'B14', 'C14', 'D14', 'E14', 'F14', 'G14', 'H14', 'J14', 'K14', 'L14', 'M14', 'N14', 'O14', 'P14',
    'Q14', 'R14', 'S14', 'T14', 'XX',
    'XX', 'A13', 'B13', 'C13', 'D13', 'E13', 'F13', 'G13', 'H13', 'J13', 'K13', 'L13', 'M13', 'N13', 'O13', 'P13',
    'Q13', 'R13', 'S13', 'T13', 'XX',
    'XX', 'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12', 'J12', 'K12', 'L12', 'M12', 'N12', 'O12', 'P12',
    'Q12', 'R12', 'S12', 'T12', 'XX',
    'XX', 'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11', 'J11', 'K11', 'L11', 'M11', 'N11', 'O11', 'P11',
    'Q11', 'R11', 'S11', 'T11', 'XX',
    'XX', 'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 'J10', 'K10', 'L10', 'M10', 'N10', 'O10', 'P10',
    'Q10', 'R10', 'S10', 'T10', 'XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'K9', 'L9', 'M9', 'N9', 'O9', 'P9', 'Q9', 'R9', 'S9',
    'T9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'K8', 'L8', 'M8', 'N8', 'O8', 'P8', 'Q8', 'R8', 'S8',
    'T8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'K7', 'L7', 'M7', 'N7', 'O7', 'P7', 'Q7', 'R7', 'S7',
    'T7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'K6', 'L6', 'M6', 'N6', 'O6', 'P6', 'Q6', 'R6', 'S6',
    'T6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'K5', 'L5', 'M5', 'N5', 'O5', 'P5', 'Q5', 'R5', 'S5',
    'T5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'K4', 'L4', 'M4', 'N4', 'O4', 'P4', 'Q4', 'R4', 'S4',
    'T4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'K3', 'L3', 'M3', 'N3', 'O3', 'P3', 'Q3', 'R3', 'S3',
    'T3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'K2', 'L2', 'M2', 'N2', 'O2', 'P2', 'Q2', 'R2', 'S2',
    'T2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1',
    'T1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'XX'
]

# поиск размеров доски
BOARDS = {
    '9': board_9x9,
    '13': board_13x13,
    '19': board_19x19
}

# поиск координат
COORDS = {
    '9': coords_9x9,
    '13': coords_13x13,
    '19': coords_19x19,
}

# камни
EMPTY = 0
BLACK = 1
WHITE = 2
MARKER = 4
OFFBOARD = 7
LIBERTY = 8

# подсчитывание свобод и групп
liberties = []
block = []

# текущая используемая доска
board = None
coords = None

# размер доски Го
BOARD_WIDTH = 0
BOARD_RANGE = 0
MARGIN = 2

# файловые маркеры
files = '     a b c d e f g h j k l m n o p q r s t'

# ASCII-представление камней
pieces = '.#o  bw +'


def print_board():
    # проходимся циклом по строкам
    for row in range(BOARD_RANGE):
        # проходимся циклом по столбцам
        for col in range(BOARD_RANGE):
            # определяем ячейку
            square = row * BOARD_RANGE + col

            # определяем камень
            stone = board[square]

            # печатаем пробелы
            if col == 0 and row > 0 and row < BOARD_RANGE - 1:
                rank = BOARD_RANGE - 1 - row
                space = '  ' if len(board) == 121 else '   '
                print((space if rank < 10 else '  ') + str(rank), end='')

            # печатаем содержимое ячейки доски
            print(pieces[stone] + ' ', end='')

        # печатаем новую линию
        print()

    # печатаем разметку
    print(('' if len(board) == 121 else ' ') + files[0:BOARD_RANGE * 2] + '\n')


# установка размеров доски
def set_board_size(command):
    # подключаем глобальные переменные
    global BOARD_WIDTH, BOARD_RANGE, board, coords

    # парсим размер доски
    size = int(command.split()[-1])

    # ошибка, если размер доски не поддерживается
    if size not in [9, 13, 19]:
        print('? current board size not supported\n')
        return

    # считаем текущий размер доски
    BOARD_WIDTH = size
    BOARD_RANGE = BOARD_WIDTH + MARGIN
    board = BOARDS[str(size)]
    coords = COORDS[str(size)]


# считаем свободы, сохраняем групповые координаты камней
def count(square, color):
    # определяем клетку
    piece = board[square]

    # пропускаем если клетка за доской
    if piece == OFFBOARD: return

    # если в клетке есть камень
    if piece and piece & color and (piece & MARKER) == 0:
        # сохраняем координаты камня
        block.append(square)

        # маркируем камень
        board[square] |= MARKER

        # ищем соседей рекурсивно
        count(square - BOARD_RANGE, color)  # север
        count(square - 1, color)  # восток
        count(square + BOARD_RANGE, color)  # юг
        count(square + 1, color)  # запад

    # если ячейка пустая
    elif piece == EMPTY:
        # маркируем свободу
        board[square] |= LIBERTY

        # записываем свободу
        liberties.append(square)


# убираем камни с доски
def clear_block():
    for captured in block: board[captured] = EMPTY


# очищаем группы
def clear_groups():
    # подключаем глобальные переменные
    global block, liberties

    # очищаем список групы и свобод
    block = []
    liberties = []

# восстанавливаем доску после подсчета камней
def restore_board():
    # очищаем группу
    clear_groups()

    # размаркеруем камни
    for square in range(BOARD_RANGE * BOARD_RANGE):
        #если клетка относится к доске  размаркеровываем
        if board[square] != OFFBOARD: board[square] &= 3 #0011 3 бит маркера будет стерт


# очистка доски
def clear_board():
    # clear groupd
    clear_groups()

    for square in range(len(board)):

        if board[square] != OFFBOARD: board[square] = 0


# делаем ход на доске
def set_stone(square, color):
    # делаем ход на доске
    board[square] = color

    # захваченные камни
    captures(3 - color)


# генеруем рандомных ход
def make_random_move(color):
    # находим свободную ячейку
    random_square = random.randrange(len(board))
    while board[random_square] != EMPTY:
        random_square = random.randrange(len(board))

    # делаем ход
    set_stone(random_square, color)

    # считаем свободы
    count(random_square, color)

    # невозможный ход
    if len(liberties) == 0:
        # восстанавливаем доску
        restore_board()

        # убираем камень
        board[random_square] = EMPTY

        # ищем другой ход
        try:
            # возвращаем легальный ход
            return make_random_move(color)
        except:
            # пропускаем ход
            return ''

            # восстанавливаем доску
    restore_board()

    # печатаем рандомный ход
    eprint('random move:', coords[random_square])

    # возвращаем ход
    return coords[random_square]


# функция игры
def play(command):
    # перебираем цвета
    color = BLACK if command.split()[1] == 'B' else WHITE

    # обрабатываем пропуск хода графического интерфейса
    if command.split()[-1] == 'pass': return

    # парсим ввод из терминала
    square_str = command.split()[-1]
    col = ord(square_str[0]) - ord('A') + 1 - (1 if ord(square_str[0]) > ord('I') else 0)
    row_count = int(square_str[1:]) if len(square_str[1:]) > 1 else ord(square_str[1:]) - ord('0')
    row = (BOARD_RANGE - 1) - row_count
    square = row * BOARD_RANGE + col

    # делаем ход
    set_stone(square, color)


# обрабатываем захваченные камни
def captures(color):
    # проходимся через все клетки
    for square in range(len(board)):
        # инициализируем клетку
        piece = board[square]

        # пропускаем клетки за игровым полем
        if piece == OFFBOARD: continue

        # если камень принадлежит данному цвету
        if piece & color:
            # считаем число свобод
            count(square, color)

            # если нет свобод - очищаем группу
            if len(liberties) == 0: clear_block()

            # восстанавливаем доску
            restore_board()


# детектируем край доски
def detect_edge(square):
    # цикл в 4 направлениях
    for direction in [BOARD_RANGE, 1, -BOARD_RANGE, -1]:
        # действительно, это край доски
        if board[square + direction] == OFFBOARD: return 1

    # не край доски
    return 0


# находим наилучшую свободу для расширения / окружения
def evaluate(color):
    # максимальное количество найденных свобод
    best_count = 0
    best_liberty = liberties[0]

    # пройдимся по свободам в списке
    for liberty in liberties:
        # кладем камень на доску
        board[liberty] = color

        # считаем новые свободы
        count(liberty, color)

        # находим больше свобод
        if len(liberties) > best_count and not detect_edge(liberty):
            best_liberty = liberty
            best_count = len(liberties)

        # восстанавливаем доску
        restore_board()

        # убираем камни с края доски
        board[liberty] = EMPTY

    # возвращаем лучшую свободу
    return best_liberty


# генерируем ход
def genmove(color):
    #######################################################################
    #
    # Логика искусственного интеллекта (сначала защита, затем атака)
    #
    # 1. Если у группы противника осталась только одна свобода - захватить его
    #
    # 2. Если группа играющей стороны имеет только одну свободу
    # сохранять эту группу, положив туда камень, если только это не край доски.
    #
    # 3. Если группа играющей стороны имеет две свободы
    # выбирай ту, которая дает больше свобод
    #
    # 4. Если у группы противника есть более одной свободы
    # попытаться окружить его
    #
    # 5. Подбирайте шаблоны, чтобы создать сильную группу, если таковые найдутся
    # отдать предпочтение этому варианту, чем гоняться за группой
    #
    #######################################################################
    best_move = 0
    capture = 0
    save = 0
    defend = 0
    surround = 0
    pattern = 0

    # захват группы
    for square in range(len(board)):
        # инициализируем клетку
        piece = board[square]

        #  подсчет группы соперника
        if piece & (3 - color):
            # подсчет числа свобод соперника
            count(square, (3 - color))

            # если 1 свобода
            if len(liberties) == 1:
                # сохранить ход захвата
                target_square = liberties[0]
                best_move = target_square
                capture = target_square
                break

            # восстановление доски
            restore_board()

    # сохранение своей группы
    for square in range(len(board)):
        # инициализируем клетку
        piece = board[square]

        # подсчет своей группы
        if piece & (color):
            # подсчет свобод своей группы
            count(square, (color))

            # если 1 свобода осталась
            if len(liberties) == 1:
                # сохранить ход спасения
                target_square = liberties[0]

                # проверка края доски
                if not detect_edge(target_square):
                    best_move = target_square
                    save = target_square
                    break

            # восстановление доски
            restore_board()

    # защита своих камней
    for square in range(len(board)):
        # инициализируем клетку
        piece = board[square]

        # подсчет своей группы
        if piece & (color):
            # считаем сколько свобод у группы
            count(square, (color))

            # если группа имеет 2 свободы
            if len(liberties) == 2:
                # сохранить ход спасения
                best_liberty = evaluate(color)
                best_move = best_liberty
                defend = best_liberty
                break

            # восстановление доски
            restore_board()

    # окружение опонента
    for square in range(len(board)):
        # инициализируем клетку
        piece = board[square]

        # подсчет группы соперника
        if piece & (3 - color):
            # подсчет свобод группы соперника
            count(square, (3 - color))

            # если группа имеет 1 свободу
            if len(liberties) > 1:
                # сохраняем ход окружения
                best_liberty = evaluate(3 - color)
                best_move = best_liberty
                surround = best_liberty

                # попробовать ход
                set_stone(best_move, color)
                count(best_move, color)
                legal = len(liberties)
                restore_board()
                board[best_move] = EMPTY
                if not legal: continue
                break

            # восстановление доски
            restore_board()

    # подсчет шаблонов
    for square in range(len(board)):
        # инициализируем клетку
        piece = board[square]

        # пропускаем клетки края доски
        if piece == OFFBOARD: continue

        # шаблон 1
        if piece & (3 - color):
            target_one = square - BOARD_RANGE + 1
            target_two = square - BOARD_RANGE - 1
            if board[target_one] & color and board[target_two] & color:
                best_move = square - BOARD_RANGE
                pattern = best_move

        # шаблон 2
        if piece & (3 - color):
            target_one = square + 1
            target_two = square - BOARD_RANGE - 1
            if board[target_one] & color and board[target_two] & color:
                best_move = square - BOARD_RANGE
                pattern = best_move

        # шаблон 3
        if piece & (3 - color):
            target_one = square + 1
            target_two = square - 1
            if board[target_one] & color and board[target_two] & color:
                best_move = square + BOARD_RANGE
                pattern = best_move

        # шаблон  4
        if piece & (3 - color):
            target_one = square - BOARD_RANGE + 2
            target_two = square - BOARD_RANGE - 1
            if board[target_one] & color and board[target_two] & color:
                best_move = square - BOARD_RANGE
                pattern = best_move

        # шаблон 5
        if piece & (3 - color):
            target_one = square - BOARD_RANGE + 2
            target_two = square - BOARD_RANGE - 2
            if board[target_one] & color and board[target_two] & color:
                best_move = square - BOARD_RANGE
                pattern = best_move

        # шаблон 6
        if piece & (3 - color):
            target_one = square - 1
            target_two = square + BOARD_RANGE - 2
            if board[target_one] & color and board[target_two] & color:
                best_move = square + BOARD_RANGE
                pattern = best_move

        # шаблон 7
        if piece & (3 - color):
            target_one = square - BOARD_RANGE
            target_two = square - BOARD_RANGE - 2
            if board[target_one] & color and board[target_two] & color:
                best_move = square - 1
                pattern = best_move

    # находим ход
    if best_move:
        # печать доступных ходов
        eprint('capture move:', coords[capture])
        eprint('save move:', coords[save])
        eprint('defend move:', coords[defend])
        eprint('surround move:', coords[surround])
        eprint('pattern move:', coords[pattern])

        # определяем рандомом действие по атаке/защите
        random_action = random.randrange(2)

        # управляем приоритетами хода ИИ
        if not capture and not defend and not save:
            best_move = surround
        elif not capture and not save and defend:
            best_move = defend if random_action else surround
        elif not capture and not defend and save:
            best_move = save
        elif pattern:
            best_move = pattern
        if save: best_move = save
        if capture: best_move = capture

        # делаем ход
        set_stone(best_move, color)

        #  подтвердите перемещение
        count(best_move, color)

        # подсчет свобод
        legal = len(liberties)

        # восстановление доски
        restore_board()

        # невозможный ход
        if not legal:
            # убираем камень с доски
            board[best_move] = EMPTY
            eprint('avoid suicide move')

            # вместо этого рассматриваем  случайный ход
            return make_random_move(color)

        eprint('best move:', coords[best_move])
        return coords[best_move]

    # если начинают черные
    return make_random_move(color)


#  Протокол связи графического интерфейса пользователя
def gtp():
    # главный бесконечный цикл графического интерфейса пользователя
    while True:
        # принять команду графического интерфейса пользователя
        command = input()
        # обработка команды
        if 'name' in command:
            print('= Wally\n')
        elif 'protocol_version' in command:
            print('= 1\n')
        elif 'version' in command:
            print('=', VERSION, '\n')
        elif 'list_commands' in command:
            print('= protocol_version\n')
        elif 'boardsize' in command:
            set_board_size(command); print('=\n')
        elif 'clear_board' in command:
            clear_board(); print('=\n')
        elif 'showboard' in command:
            print('= '); print_board()
        elif 'play' in command:
            play(command); print('=\n')
        elif 'genmove' in command:
            print('=', genmove(BLACK if command.split()[-1] == 'B' else WHITE) + '\n')
        elif 'quit' in command:
            sys.exit()
        else:
            print('=\n')  # пропускаем неподдерживаемые команды


# запуск связи графического интерфейса пользователя
gtp()











