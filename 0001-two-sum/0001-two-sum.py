class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm={}

        for i,n in enumerate(nums):
            d = target - n
            if d in hashm:
                return hashm[d],i
            hashm[n]=i
        return