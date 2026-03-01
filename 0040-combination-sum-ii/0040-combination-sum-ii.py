class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def sum2(start, curr, curr_sum):
            if curr_sum == target:
                res.append(list(curr))
                return
            if curr_sum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                sum2(i + 1, curr, curr_sum + candidates[i])
                curr.pop()
        sum2(0, [], 0)
        return res