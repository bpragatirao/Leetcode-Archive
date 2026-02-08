class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        o,c = 0,0
        res,l = [],[]

        for i in range(len(s)):
            if s[i]=="(":
                o+=1
            elif s[i]==")":
                c+=1
            l.append(s[i])
            
            if o==c:
                res.append("".join(l))
                l = []
                o,c = 0,0

        result = []
        for i in res:
            result.append(i[1:len(i)-1])
        
        return "".join(result)
        