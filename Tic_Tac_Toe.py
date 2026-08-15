board = [' '] * 9


def print_board():
    print()
    for i in range(3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        if i < 2:
            print('--+---+--')
    print()


def check_winner(player):
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


player = 'X'

for turn in range(9):

    print_board()

    position = int(input(
        f"Player {player}, enter position (0-8): "
    ))

    if position < 0 or position > 8:
        print("Invalid position!")
        continue

    if board[position] != ' ':
        print("Position already occupied!")
        continue

    board[position] = player

    if check_winner(player):
        print_board()
        print("Player", player, "wins!")
        break

    player = 'O' if player == 'X' else 'X'

else:
    print_board()
    print("Game Draw!")