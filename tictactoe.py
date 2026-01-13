# Tic Tac Toe Game (Console)

board = [" " for _ in range(9)]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return " " not in board

def game():
    current_player = "X"
    print("Tic Tac Toe")
    print("Positions: 1 2 3 | 4 5 6 | 7 8 9")

    while True:
        print_board()
        move = input(f"Player {current_player}, choose position (1-9): ")

        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Invalid input. Try again.")
            continue

        move = int(move) - 1
        if board[move] != " ":
            print("Position already taken. Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

game()
