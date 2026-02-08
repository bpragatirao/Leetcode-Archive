class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        r,c = 0,m-1

        while r<n and c>=0:
            for i in matrix:
                if target in i:
                    return True
            r+=1
        return False
        