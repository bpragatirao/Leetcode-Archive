class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def subs(start,sub):
            res.append(list(sub))

            for i in range(start,len(nums)):
                if i> start and nums[i]==nums[i-1]:
                    continue

                sub.append(nums[i])
                subs(i+1,sub)
                sub.pop()
        subs(0,[])
        return res