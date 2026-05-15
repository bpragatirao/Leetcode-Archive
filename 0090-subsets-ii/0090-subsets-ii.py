class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def subs(i,sub):
            res.append(list(sub))

            for j in range(i,len(nums)):
                if j> i and nums[j]==nums[j-1]:
                    continue

                sub.append(nums[j])
                subs(j+1,sub)
                sub.pop()
        subs(0,[])
        return res
