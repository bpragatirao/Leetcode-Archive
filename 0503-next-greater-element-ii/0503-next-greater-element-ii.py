class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        def nextgr(n,s):
            for i in s:
                if i>n:
                   return i
            return -1
        
        for i in range(len(nums)):
            res.append(nextgr(nums[i],nums[i+1:]+nums[:i]))
        
        return res if len(res)==len(nums) else []