class Solution:
    def maxDepth(self, s: str) -> int:
        max1,max2 = 0,0

        for i in s:
            if i=="(":
                max1+=1
                if max1>max2:
                    max2 = max1
            elif i==")":
                max1-=1
        return max2