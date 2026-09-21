def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solve_n_queen(board, row, N):
    if row == N:
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queen(board, row + 1, N):
                return True
            board[row][col] = 0
    return False

def print_board(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()

def solve_n_queen_problem(N):
    board = [[0] * N for _ in range(N)]
    if solve_n_queen(board, 0, N) is False:
        print("No solution exists for N =", N)

for _ in range(3):
    N = int(input("Enter the number of queens (N): "))
    solve_n_queen_problem(N)