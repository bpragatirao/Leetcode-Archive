import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mheap = nums[:k]
        heapq.heapify(mheap)

        for i in range(k,len(nums)):
            if nums[i]> mheap[0]:
                heapq.heapreplace(mheap,nums[i])
        
        return mheap[0]

