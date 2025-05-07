def solve_sudoku(board):
    def is_valid(r, c, n):
        
        for i in range(9):
            if board[r][i] == n or board[i][c] == n:
                return False
        
        sr, sc = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                if board[sr + i][sc + j] == n:
                    return False
        return True

    def backtrack():
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:  
                    for n in range(1, 10):
                        if is_valid(r, c, n):
                            board[r][c] = n
                            if backtrack():  
                                return True
                            board[r][c] = 0  
                    return False
        return True  

    backtrack()  
    return board  

