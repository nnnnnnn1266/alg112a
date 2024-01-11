#使用chatgpt
#八皇后問題是一個在8×8的棋盤上放置8個皇后，使得彼此之間不能互相攻擊（即不能在同一行、同一列或同一對角線上）的問題。

def is_safe(board, row, col, n):
    # 檢查同一列是否有皇后
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # 檢查左上到右下的對角線是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # 檢查左下到右上的對角線是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # 將合法解加入結果列表
        solutions.append(["".join(["Q" if cell == 1 else "." for cell in row]) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0  # 回溯

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

# 求解八皇后問題
eight_queens_solutions = solve_n_queens(8)
for idx, solution in enumerate(eight_queens_solutions):
    print(f"Solution {idx + 1}:\n")
    for row in solution:
        print(row)
    print("\n" + "=" * 20 + "\n")
