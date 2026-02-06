class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = (sum(piles) + h - 1) // h
        high = max(piles)
        
        while low < high:
            k = (low + high) // 2

            total_h = sum((p + k - 1) // k for p in piles)
            
            if total_h <= h:
                high = k 
            else:
                low = k + 1 
                
        return low