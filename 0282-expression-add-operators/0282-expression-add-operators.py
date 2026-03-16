class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def solve(i, path, curr_res, prev_val):
            if i == len(num):
                if curr_res == target:
                    res.append(path)
                return

            for j in range(i, len(num)):
                if j > i and num[i] == '0':
                    break
                
                curr_str = num[i : j + 1]
                curr_val = int(curr_str)

                if i == 0:
                    solve(j + 1, curr_str, curr_val, curr_val)
                else:
                    solve(j + 1, path + "+" + curr_str, curr_res + curr_val, curr_val)
                    
                    solve(j + 1, path + "-" + curr_str, curr_res - curr_val, -curr_val)

                    solve(j + 1, path + "*" + curr_str, (curr_res - prev_val) + (prev_val * curr_val), prev_val * curr_val)

        solve(0, "", 0, 0)
        return res