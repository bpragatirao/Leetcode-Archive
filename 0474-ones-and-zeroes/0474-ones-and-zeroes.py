class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0,0): 0}

        for s in strs:
            p = 0
            q = 0
            for j in s:
                if j == "0":
                    p+=1
                elif j == "1":
                    q+=1
            
            newdp = {}

            for k,v in dp.items():
                prevp, prevq = k
                newp, newq = prevp + p, prevq + q
                if newp <= m and newq <= n:
                    if (newp, newq) not in dp:
                        newdp[(newp, newq)] = v + 1
                    elif dp[(newp, newq)] < v + 1:
                        newdp[(newp, newq)] = v + 1
            dp.update(newdp)
        return max(dp.values())