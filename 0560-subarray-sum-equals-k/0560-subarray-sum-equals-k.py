class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashm = {0: 1}
        cnt = 0
        sumi = 0
        for i in range(len(nums)):
            sumi+=nums[i]
            d = sumi-k
            if d in hashm:
                cnt += hashm[d]
            hashm[sumi] = hashm.get(sumi,0)+1
        return cnt