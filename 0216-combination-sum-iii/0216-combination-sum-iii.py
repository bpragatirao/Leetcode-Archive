class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def valid(start,sub,curr_sum):
            if len(sub)==k:
                if curr_sum == n:
                    res.append(sub.copy())
                    return
            
            if curr_sum > n:
                return

            for i in range(start,10):
                sub.append(i)
                valid(i+1,sub,curr_sum+i)
                sub.pop()

        valid(1,[],0)
        return res