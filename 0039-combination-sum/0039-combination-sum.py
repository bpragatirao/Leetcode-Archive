class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur_subset, total):
            if total == target:
                res.append(cur_subset.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur_subset.append(candidates[i])
            dfs(i, cur_subset, total + candidates[i])
            cur_subset.pop()
            dfs(i + 1, cur_subset, total)
        dfs(0, [], 0)
        return res
        