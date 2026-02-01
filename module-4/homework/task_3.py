def print_board(board):
    print("\nМаршрут коня:")
    for row in board:
        print(" ".join(f"{x:2d}" for x in row))

def is_valid(x, y, board):
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1

def solve_knight_tour(board, x, y, move_num, moves):
    if move_num == 64:
        return True

    for dx, dy in moves:
        next_x = x + dx
        next_y = y + dy
        if is_valid(next_x, next_y, board):
            board[next_x][next_y] = move_num
            if solve_knight_tour(board, next_x, next_y, move_num + 1, moves):
                return True
            
            board[next_x][next_y] = -1

    return False

def main():
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    board = [[-1 for _ in range(8)] for _ in range(8)]

    print("Введите начальные координаты коня (от 1 до 8):")
    try:
        start_x = int(input("Строка (горизонталь, 1–8): ")) - 1
        start_y = int(input("Столбец (вертикаль, 1–8): ")) - 1
    except ValueError:
        print("Ошибка: введите числа от 1 до 8.")
        return

    if not (0 <= start_x < 8 and 0 <= start_y < 8):
        print("Ошибка: координаты должны быть от 1 до 8.")
        return

    board[start_x][start_y] = 0

    print(f"\nИщем маршрут с клетки ({start_x + 1}, {start_y + 1})...")

    if solve_knight_tour(board, start_x, start_y, 1, moves):
        print_board(board)
    else:
        print("Маршрут не найден. (Для некоторых начальных клеток решения нет.)")

main()