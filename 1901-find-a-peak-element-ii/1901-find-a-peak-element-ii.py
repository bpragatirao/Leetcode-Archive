class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n,m = len(mat),len(mat[0])  
        low = 0
        high = m - 1
        
        while low <= high:
            mid = (low + high) // 2

            max_row = 0
            for r in range(1, n):
                if mat[r][mid] > mat[max_row][mid]:
                    max_row = r

            left_val = mat[max_row][mid - 1] if mid > 0 else -1
            right_val = mat[max_row][mid + 1] if mid < m - 1 else -1
            if mat[max_row][mid] > left_val and mat[max_row][mid] > right_val:
                return [max_row, mid]
            
            elif left_val > mat[max_row][mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        return []