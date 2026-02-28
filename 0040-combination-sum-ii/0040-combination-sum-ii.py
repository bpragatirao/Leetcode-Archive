class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def sum2(start, current_subset, current_sum):
            if current_sum == target:
                res.append(list(current_subset))
                return
            if current_sum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current_subset.append(candidates[i])
                sum2(i + 1, current_subset, current_sum + candidates[i])
                current_subset.pop()
        sum2(0, [], 0)
        return res