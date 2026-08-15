# Tic Tac Toe AI - CodSoft Task 2

board = [" " for i in range(9)]


def show_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_places = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for place in winning_places:
        if board[place[0]] == player and board[place[1]] == player and board[place[2]] == player:
            return True

    return False


def board_full():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if board_full():
        return 0

    if is_maximizing:
        best_score = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def computer_move():
    best_score = -100
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


print("🎮 Welcome to Tic-Tac-Toe!")
print("You are X and Computer is O.")
print("Choose a position from 1 to 9.")

while True:
    show_board()

    try:
        position = int(input("Enter your position (1-9): "))
    except ValueError:
        print("Please enter a number.")
        continue

    if position < 1 or position > 9:
        print("Please choose a number between 1 and 9.")
        continue

    position = position - 1

    if board[position] != " ":
        print("This position is already taken.")
        continue

    board[position] = "X"

    if check_winner("X"):
        show_board()
        print("🎉 You won!")
        break

    if board_full():
        show_board()
        print("It's a draw!")
        break

    computer_move()

    if check_winner("O"):
        show_board()
        print("🤖 Computer won!")
        break

    if board_full():
        show_board()
        print("It's a draw!")
        break 