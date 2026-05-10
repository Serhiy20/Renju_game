BOARD_SIZE = 19
MAX_TESTS = 11
WIN_LENGTH = 5

DIRECTIONS = [
    (0, 1, "горизонтально"),
    (1, 0, "вертикально"),
    (1, 1, "діагональ ↘"),
    (1, -1, "діагональ ↙")
]

def in_bounds(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def is_same_color(board, x, y, color):
    return in_bounds(x, y) and board[x][y] == color

def check_winner(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                continue

            color = board[i][j]

            for dx, dy, name in DIRECTIONS:
                count = 1
                nx, ny = i + dx, j + dy

                while is_same_color(board, nx, ny, color):
                    count += 1
                    nx += dx
                    ny += dy

                if count == WIN_LENGTH:
                    px, py = i - dx, j - dy

                    if is_same_color(board, px, py, color):
                        continue

                    if is_same_color(board, nx, ny, color):
                        continue

                    return color, i + 1, j + 1, name

    return 0, None, None, None

def read_board():
    print(f"Вставте {BOARD_SIZE} рядків (по {BOARD_SIZE} чисел):")
    board = []
    while len(board) < BOARD_SIZE:
        row = list(map(int, input().split()))
        if len(row) != BOARD_SIZE:
            print(f"Потрібно рівно {BOARD_SIZE} чисел")
            continue
        board.append(row)
    return board

def main():
    t = int(input(f"Кількість тестів (1-{MAX_TESTS}): "))

    for test in range(1, t + 1):
        print(f"\n=== Тест {test} ===")

        board = read_board()
        winner, x, y, direction = check_winner(board)

        print("\nРезультат:")
        if winner == 0:
            print("0")
            print("\nНіхто не виграв — немає послідовності рівно з 5 каменів.")
        else:
            print(winner)
            print(f"{x} {y}")

            player = "чорні" if winner == 1 else "білі"

            print(f"\nВиграли {player}, зібравши {WIN_LENGTH} каменів підряд ({direction}).")
            print(f"Початок послідовності (координати першого каменя з п’ятірки): рядок {x}, колонка {y}.")

if __name__ == "__main__":
    main()
