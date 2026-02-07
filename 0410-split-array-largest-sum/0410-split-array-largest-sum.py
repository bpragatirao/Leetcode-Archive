class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = max(nums),sum(nums)
        res = 0

        def canSplit(mid):
            s,t = 0,1
            for i in nums:
                if s+i > mid:
                    t+=1
                    s=i
                else:
                    s+=i
            if t<=k:
                return True
            return False

        while l<=r:
            mid = (l+r)//2

            if canSplit(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1

        return res if res else 0