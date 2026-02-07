class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        l,r = min(bloomDay),max(bloomDay)
        res = 0

        def canMake(day):
            bouquets = 0
            flowers = 0
            for b in bloomDay:
                if b <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                
                if bouquets >= m:
                    return True
            return False

        while l<=r:
            mid = (l+r)//2

            if canMake(mid):
                res = mid
                r = mid-1
            else:
                l=mid+1

        return -1 if m*k > n else res