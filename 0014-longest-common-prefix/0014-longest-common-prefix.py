class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs=sorted(strs)
        l=strs[0]
        r=strs[-1]
        for i in range(min(len(l),len(r))):
            if(l[i]!=r[i]):
                return res
            res+=l[i]
        return res