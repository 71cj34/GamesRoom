# deprecated

import random

board = [["·", "·", "·"], ["·", "·", "·"], ["·", "·", "·"]]
pieces = ["×", "⦿"]

def print_board():
    for row in board:
        print(*row)

def check_win(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def board_full():
    for row in board:
        if "·" in row:
            return False
    return True

def get_empty_cells():
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "·":
                empty_cells.append((i, j))
    return empty_cells

def minimax(board, depth, maximizing, player, opponent):
    if check_win(player):
        return 10 - depth
    if check_win(opponent):
        return depth - 10
    if board_full():
        return 0

    if maximizing:
        best_score = -float('inf')
        for i, j in get_empty_cells():
            board[i][j] = player
            score = minimax(board, depth + 1, False, player, opponent)
            board[i][j] = "·"
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_empty_cells():
            board[i][j] = opponent
            score = minimax(board, depth + 1, True, player, opponent)
            board[i][j] = "·"
            best_score = min(score, best_score)
        return best_score

def get_best_move(player, opponent, difficulty):
    best_score = -float('inf')
    best_move = None
    for i, j in get_empty_cells():
        board[i][j] = player
        if check_win(player):
            board[i][j] = "·"
            return (i, j)
        score = minimax(board, 0, False, player, opponent)
        board[i][j] = "·"
        if score > best_score:
            best_score = score
            best_move = (i, j)

    if difficulty == "easy":
        if random.random() < 0.5:
            return random.choice(get_empty_cells())
    elif difficulty == "medium":
        if random.random() < 0.25:
            return random.choice(get_empty_cells())

    return best_move

def play_tictactoe():
    global board
    board = [["·", "·", "·"], ["·", "·", "·"], ["·", "·", "·"]]

    player_piece = input("Choose your piece (× or ⦿): ")
    while player_piece not in pieces:
        player_piece = input("Invalid choice. Choose your piece (× or ⦿): ")
    print("AI moves first." if player_piece == "⦿" else "")

    ai_piece = "⦿" if player_piece == "×" else "×"

    difficulty = input("Choose AI difficulty (easy/medium/hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("Invalid choice. Choose AI difficulty (easy/medium/hard): ").lower()

    current_player = "×"

    while True:
        print_board()
        if current_player == player_piece:
            while True:
                try:
                    row, col = map(int, input("Enter your move (row col): ").split())
                    row -= 1
                    col -= 1
                    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "·":
                        board[row][col] = player_piece
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Try again.")
        else:
            row, col = get_best_move(ai_piece, player_piece, difficulty)
            board[row][col] = ai_piece
            print(f"AI plays: {row + 1} {col + 1}")

        if check_win(current_player):
            print_board()
            print('You win!' if current_player == player_piece else 'AI wins!')
            break
        elif board_full():
            print_board()
            print("It's a tie!")
            break

        current_player = ai_piece if current_player == player_piece else player_piece

if __name__ == "__main__":
    play_tictactoe()

# def printboard():
#     print(*b[0])
#     print(*b[1])
#     print(*b[2])

