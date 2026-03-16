
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = Counter(nums)
        
        for i,k in enumerate(n):
            if n[k]<2:
                return k