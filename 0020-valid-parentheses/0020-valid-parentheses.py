class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        top = -1
        for i in s:
            if i in ["(","{","["]:
                l.append(i)
            elif i in [")","}","]"]:
                if len(l) == 0:
                    return False
                    
                if i == ")" and l[top]=="(":
                    l.pop()
                elif i == "}" and l[top]=="{":
                    l.pop()
                elif i == "]" and l[top]=="[":
                    l.pop()
                else: 
                    return False
        if len(l)==0:
            return True
        else:
            return False