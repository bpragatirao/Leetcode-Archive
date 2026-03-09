class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def safe(r, c, board, n):
            dr, dc = r, c
            while (r >= 0 and c >= 0):
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            
            r, c = dr, dc
            while c >= 0:
                if board[r][c] == "Q":
                    return False
                c -= 1

            r, c = dr, dc
            while (r < n and c >= 0):
                if board[r][c] == "Q":
                    return False
                r += 1
                c -= 1
            return True

        def solve(col, board, res, n):
            if col == n:
                res.append(["".join(row) for row in board])
                return

            for row in range(n):
                if safe(row, col, board, n):
                    board[row][col] = "Q"
                    solve(col + 1, board, res, n)
                    board[row][col] = "."

        res = []
        board = [["."] * n for i in range(n)]
        solve(0, board, res, n)
        return res
