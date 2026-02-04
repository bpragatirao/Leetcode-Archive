class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 0
        nums.sort()
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                j = i+1
                while j in nums:
                    j+=1
                k = max(k,j-i)
        return k
            
        return len(res)