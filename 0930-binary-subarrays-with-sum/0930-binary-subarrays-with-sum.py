class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k < 0: return 0
            left = res = cur = 0
            for right in range(len(nums)):
                cur += nums[right]
                while cur > k:
                    cur -= nums[left]
                    left += 1
                res += right - left + 1
            return res
    
        return atMost(goal) - atMost(goal - 1)