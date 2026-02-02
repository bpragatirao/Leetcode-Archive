from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums)//2
        c = Counter(nums)
        for i in c:
            if c[i]>mid:
                return i
