from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        if not arr:
            return 
        res = []
        for i in d:
            if d[i]==i:
                res.append(i)
        r = 0
        for i in res:
            if i>r:
                r=i
                
        return r if r else -1
