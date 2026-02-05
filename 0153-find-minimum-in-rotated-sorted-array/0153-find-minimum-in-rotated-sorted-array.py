class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        mini = float('inf')

        while l<=r:
            if nums[l]<=nums[r]:
                mini = min(mini,nums[l])
                break
                
            mid = (l+r)//2
            mini = min(mini,nums[mid])

            if nums[l]<=nums[mid]:
                mini = min(mini,nums[l])
                l = mid+1
                
            else:
                r = mid-1

        return mini
                