class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n = max(nums)

        if len(nums) != n+1:
            return False
        
        from collections import Counter
        cnts = Counter(nums)

        for i in range(1,n):
            if cnts[i] != 1:
                return False

        return cnts[n] == 2