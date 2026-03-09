class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r,c = len(board),len(board[0])
        def check(l,n,i):
            if i==len(word):
                return True

            if (l<0 or l>=r or n<0 or n>=c or board[l][n]!=word[i]):
                return False

            temp = board[l][n]
            board[l][n] = "#"

            res = (check(l+1,n,i+1) or check(l-1,n,i+1) or check(l,n+1,i+1) or check(l,n-1,i+1))
            board[l][n] = temp

            return res

        for i in range(r):
            for j in range(c):
                if check(i,j,0):
                    return True  
        return False