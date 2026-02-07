class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        l,r = max(weights),sum(weights)
        res = 0

        def cargo(mid):
            w,d = 0,1
            for i in weights:
                if w+i>mid:
                    d+=1
                    w=i
                else:
                    w+=i
                
            if d<=days:
                return True
            return False

        while l<=r:
            mid = (l+r)//2

            if cargo(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res if res else 0
        