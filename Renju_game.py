directions = [
    (0, 1, "горизонтально"),
    (1, 0, "вертикально"),
    (1, 1, "діагональ ↘"),
    (1, -1, "діагональ ↙")
]

def check_winner(board):
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue

            color = board[i][j]

            for dx, dy, name in directions:
                count = 1
                nx, ny = i + dx, j + dy

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                    count += 1
                    nx += dx
                    ny += dy

                if count == 5:
                    px, py = i - dx, j - dy
                    if 0 <= px < 19 and 0 <= py < 19 and board[px][py] == color:
                        continue

                    if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                        continue

                    return color, i + 1, j + 1, name

    return 0, None, None, None

def read_board():
    print("Вставте 19 рядків (по 19 чисел):")
    board = []
    while len(board) < 19:
        row = list(map(int, input().split()))
        if len(row) != 19:
            print("Потрібно рівно 19 чисел")
            continue
        board.append(row)
    return board

def main():
    t = int(input("Кількість тестів (1-11): "))

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

            if winner == 1:
                player = "чорні"
            else:
                player = "білі"

            print(f"\nВиграли {player}, зібравши 5 каменів підряд ({direction}).")
            print(f"Початок послідовності: рядок {x}, колонка {y}.")

if __name__ == "__main__":
    main()
