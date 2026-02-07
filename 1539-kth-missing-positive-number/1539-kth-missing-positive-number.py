class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = []
        i = 1
        while arr:
            if i not in arr:
                res.append(i)
            
            if len(res)>k:
                return res[k-1]
   
            i+=1