class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxc,maxl = nums[0],nums[0]
        for i in range(1,len(nums)):
            maxc = max(nums[i], maxc+nums[i])
            maxl = max(maxc,maxl)
        return maxl