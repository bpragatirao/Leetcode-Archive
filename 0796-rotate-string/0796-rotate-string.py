class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True

        k=1
        while k<=len(s):
            if s[k:]+s[:k] == goal:
                return True
            k+=1
        return False