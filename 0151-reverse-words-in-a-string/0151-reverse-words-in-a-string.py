class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split())
        res,result = l,[]

        for i in range(len(res)-1,-1,-1):
            if i == 0:
                result.append(res[i])
            else:
                result.append(res[i]+" ")
        return "".join(result)
