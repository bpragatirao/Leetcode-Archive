class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def func(k):
            l,res = 0,0
            c,odd = 0,0

            for r in range(len(nums)):
                if nums[r]%2!=0:
                    odd+=1

                while odd>k:
                    if nums[l]%2!=0:
                        odd-=1
                    l+=1

                res += (r-l+1) 
            return res
        
        return func(k) - func(k-1)