class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero = False

        for i in range(m):
            if matrix[i][0]==0:
                zero=True
            for j in range(1,n):
                s = matrix[i][j]
                if s==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if zero:
                matrix[i][0]=0
                
        