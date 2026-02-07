class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r = 0,max(nums)
        ans = r
        while l<=r:
            mid = (l+r)//2

            sumi = 0
            if mid == 0: 
                l = 1
                continue
            for i in nums:
                sumi+= (i+mid-1)//mid

            if sumi<=threshold:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
        