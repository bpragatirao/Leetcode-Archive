class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m = len(board),len(board[0])
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        empty_cells = []

        for r in range(n):
            for c in range(m):
                val = board[r][c]
                if val != ".":
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[3 * (r // 3) + (c // 3)].add(val)
                else:
                    empty_cells.append((r, c))

        def solve(i):
            if i == len(empty_cells):
                return True
            
            r, c = empty_cells[i]
            box_idx = 3 * (r // 3) + (c // 3)
            
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)
                    
                    if solve(i + 1):
                        return True

                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
                    board[r][c] = "."
            
            return False

        solve(0)