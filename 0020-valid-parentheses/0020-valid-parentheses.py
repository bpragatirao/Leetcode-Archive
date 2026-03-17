class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        top = -1
        for i in s:
            if i in ["(","{","["]:
                res.append(i)
            elif i in [")","}","]"]:
                if len(res) == 0:
                    return False
                    
                if i == ")" and res[top]=="(":
                    res.pop()
                elif i == "}" and res[top]=="{":
                    res.pop()
                elif i == "]" and res[top]=="[":
                    res.pop()
                else: 
                    return False
        if len(res)==0:
            return True
        else:
            return False